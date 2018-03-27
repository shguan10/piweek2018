import io
import socket
import _thread
import struct
import tempfile
import datetime
import pathlib
from db_ops import update_django
import classify_image as ci
import os
from pprint import pprint as pp
from time import sleep
from mapper import map_item
def on_new_client(conn, addr):
    connection = conn.makefile('rb')
    directory = tempfile.TemporaryDirectory()
    user_id = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
    print(directory)
    print(user_id)
    frames_received=0
    while True:
        # Read the length of the image as a 32-bit unsigned int. If the length is zero, quit the loop
        try:
          image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        except:
          connection.close()
          print("exiting due to unpack failure")
          return

        print(image_len)
        if not image_len:
            break
            
        dt = datetime.datetime.now()
        file = directory.name + "/" + dt.strftime("%s")
               
        # Construct a stream to hold the image data and read the image data from the connection
        with open(file, 'wb') as file_stream:
           file_stream.write(connection.read(image_len))
        frames_received+=1
    # Hit the Tensor
    #sleep(frames_received+1)
    print("hitting tensor like it was a piece of meat")
    #print(os.listdir(directory.name))
    files = os.listdir(directory.name)
    files = sorted(files, key=lambda x: int(x))
    ci.create_graph()
    startfile = files[0]
    endfile = files[-1]
    midway = (int(endfile)+3*int(startfile))/4
    print(midway)
    found=False
    for fname in files:
        print(directory.name+'/'+fname)
        #import shutil
        #shutil.copyfile(directory.name+'/'+fname,'tmp.jpg')
        preds=ci.identify(directory.name+'/'+fname)
        pp(preds)
        for pred in preds:
            a=map_item(pred[0])
            print(a)
            if (a is not None) and (pred[1]>0.2):
                update_django(a,int(fname)<midway,user_id)
                with open('log','a') as f:
                    print('update_django(%s,%s,%d)' % (a,str(int(fname)<midway),user_id),file=f)

                found=True#TODO assumes that each transaction involves strictly one food item
                break
        if found: break        

    connection.close()
    print("pseudo-SIGINT received")


# Start a socket listening for connections on 0.0.0.0:8000
with socket.socket() as server_socket:
    server_socket.bind(('0.0.0.0', 8000))
    server_socket.listen(0)

    while True:
        conn, addr = server_socket.accept()
        _thread.start_new_thread(on_new_client, (conn, addr))
