import numpy as np
import cv2
cv=cv2
import sys

def largest_white_contour_bbox(image_file_name="light.jpg",im=None):
  """function accepts either an image file name or a numpy array representing a greyscale image
  """
  if im is None:
    im = cv2.imread(image_file_name)
  imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
  ret, thresh = cv2.threshold(imgray, 127, 255, 0)
  im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  cont_areas = [cv2.contourArea(cnt) for cnt in contours]
  cnt = contours[np.argmax(cont_areas)]

  # imout=cv2.drawContours(im, [cnt], 0, (0,255,0), 3)
  # cv2.imshow('contour',im)
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()

  x,y,w,h = cv2.boundingRect(cnt)

  # cv2.rectangle(im,(x,y),(x+w,y+h),(0,255,0),2)
  # cv2.imshow('bbox',im)
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()
  return (x,y,w,h)


def infer_direction(camera):
  """camera input must have read(), isOpened()
    read() returns a numpy array representing the image
    isOpened() returns whether there are still images left to process
  """
  # cv.namedWindow("tracking")
  ok, image=camera.read()
  if not ok:
    print('Failed to read video')
    exit()
  bbox = largest_white_contour_bbox(im=image)
  tracker = cv.TrackerKCF_create()
  init_once = False
  while camera.isOpened():
    ok, image=camera.read()
    if not ok:
        print('no image to read')
        break

    if not init_once:
        ok = tracker.init(image, bbox)
        init_once = True

    ok, newbox = tracker.update(image)
    print(ok, newbox)

    # if ok:
    #     p1 = (int(newbox[0]), int(newbox[1]))
    #     p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
    #     cv.rectangle(image, p1, p2, (200,0,0))

    # cv.imshow("tracking", image)
    # k = cv.waitKey(1) & 0xff
    # if k == 27 : break # esc pressed

def main():
  camera = cv.VideoCapture(sys.argv[1])
  direction=infer_direction(camera)
  print("went this way")
  print(direction)
  return direction

if __name__=="__main__": main()