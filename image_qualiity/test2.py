import cv2
import sys

path = sys.argv[1]
  
# Using cv2.imread() method 
img = cv2.imread(path) 
  
# Displaying the image 
# cv2.imshow('image', img) 

a = cv2.quality.QualityBRISQUE.compute(img)
print (a)