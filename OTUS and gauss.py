import cv2
import os
import numpy as np

image_path = os.path.abspath('/Users/yirui/Desktop/code/opencv/1.jpeg')
img = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img,(0,0),fx=0.8,fy=0.8)

thresh=127
maxval=255

ret, th1=cv2.threshold(img,thresh,maxval, cv2.THRESH_TOZERO)
ret, th2= cv2.threshold(img, thresh, maxval,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
th3 = cv2.adaptiveThreshold(img,maxval,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
th4 = cv2.adaptiveThreshold(img,maxval,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,5)


cv2.imshow('gary',img)
cv2.imshow('2',th1)
cv2.imshow('otsu',th2)
cv2.imshow('mean',th3)
cv2.imshow('gauss',th4)

print(f"threshold={ret}")

cv2.waitKey(0)
cv2.destroyAllWindows()
