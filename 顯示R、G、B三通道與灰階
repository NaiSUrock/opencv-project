import cv2
import os
import sys
print(sys.path)

image_path = os.path.abspath('/Users/yirui/Desktop/code/opencv/1.jpeg') 
img_gray = cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
img = cv2.imread(image_path)

img_red = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
img_red[:, :, 0] = 0  
img_red[:, :, 1] = 0  

img_blue = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
img_blue[:, :, 2] = 0
img_blue[:, :, 1] = 0

img_green = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)
img_green[:, :, 2] = 0
img_green[:, :, 0] = 0

cv2.imshow('red',img_red)
cv2.imshow('blue',img_blue)
cv2.imshow('green',img_green)
cv2.imshow('gray',img_gray)
cv2.imshow('original',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
