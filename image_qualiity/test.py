import cv2
import sys
vidPath = sys.argv[1]
cam = cv2.VideoCapture(vidPath)

# frame 
currentframe = 0
# reading from frame 
ret,frame = cam.read() 

if ret:
    dis = frame
    cv2.imwrite("frame.png", frame) 
# dis = cv2.imread(imgPath, 1)
if(dis is None):
    print("Wrong image path given")
    print("Exiting...")
    sys.exit(0)