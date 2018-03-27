#!/usr/bin/python3 
# improved from the sh*tty code provided at https://github.com/pageauc/picamera-motion/blob/master/picamera-motion.py
import numpy as np
import os 
import datetime 
import time 
import glob 
import picamera 
import picamera.array

from PIL import Image

import io
import socket
import struct

#=========== 
#Constants

TMP_IMAGE_DIR='~/imagedir'
(streamWidth, streamHeight)=(200,200)
sqthreshold=120000
SERVER_IP = '13.58.246.18'
SERVER_PORT = 8000
USER_ID = 6
#==========

def get_now():
  """ Get datetime and return formatted string"""
  right_now = datetime.datetime.now()
  return ("%04d%02d%02d-%02d:%02d:%02d"
      % (right_now.year, right_now.month, right_now.day,
         right_now.hour, right_now.minute, right_now.second))


def get_stream_array(camera):
  """ Take a stream image and return the image data array"""
  with picamera.array.PiRGBArray(camera) as stream:
     camera.capture(stream, format='rgb')
     return stream.array

def scan_motion(camera):
  """ Loop until motion is detected """
  data1 = get_stream_array(camera)
  while True:
    data2 = get_stream_array(camera)
    print("comparing data1 and data2")
    diff=np.sum((data1-data2)**2)
    if diff>sqthreshold: return True
    else: data1 = data2

def is_motion(data1,data2):
  """
  ACCEPTS:
    data1 and data2 are bytes encoding a jpg of the same dimensions
  RETURNS True if there is motion, False otherwise    
  """
  print("looking for motion")
  with Image.open(io.BytesIO(data1)) as pilimg1:
    arr1 = np.array(pilimg1)
    with Image.open(io.BytesIO(data2)) as pilimg2:
      arr2 = np.array(pilimg2)
      diff=np.sum((arr1-arr2)**2)
  return diff>sqthreshold

def write_when_motion_detected():
  """
  Loop until motion found then write to the network stream, 
  checking intermittengly for motion, and when motion has 
  not been detected for more than 5 seconds, then stop writing 
  and continue motion detection
  """
  with picamera.PiCamera() as camera:
    camera.resolution=(streamWidth, streamHeight)
    camera.start_preview()
    time.sleep(2)
    while True:
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        with client_socket.makefile('wb') as connection:
          scan_motion(camera)
          print("detected motion; writing to network stream")
          stream = io.BytesIO()
          connection.write(struct.pack('<L',USER_ID))
          check=0
          prev_png=None
          for _ in camera.capture_continuous(stream,'jpeg'):
            print(check)
            le=stream.tell()
            # print(le)
            connection.write(struct.pack('<L',le))
            connection.flush()

            stream.seek(0)
            png=stream.read()
            connection.write(png)

            if check and not (check % 10):
              prev_png=png
            if check is not 1 and not (check-1)%10:
              if not is_motion(prev_png,png): break

            stream.seek(0)
            stream.truncate()
            check+=1

          connection.write(struct.pack('<L',0))
          connection.flush()

if __name__=='__main__':
  write_when_motion_detected()
