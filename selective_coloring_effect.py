#cv2.__version__ '4.5.1'
from cv2 import cv2
import numpy as np

#initializing boundaries of mask
lower = np.array([0,0,0], dtype = np.uint8)
upper = np.array([0,0,0], dtype = np.uint8)

# Morphological Transform, Dilation for each color and bitwise_and operator 
# between imageFrame and mask determines to detect only that particular color
kernal = np.ones((5, 5), "uint8")

#function of clicking and processing the event
def click(event,x,y,flags,param):
    global lower, upper #should be global for streaming
    if event == cv2.EVENT_LBUTTONDOWN:
        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
        hsv_color = hsvFrame[x,y] #HSV color of coordinate (x,y)

        #Uncomment if you want to see the color and coordinate of click event
        #print('X:',x,' ','Y:',y)
        #print('hsvcolor:', hsv_color)

        #storing boundaries of mask
        lower = np.array([hsv_color[0]-20, hsv_color[1]-20, hsv_color[2]-20], dtype = np.uint8)
        upper = np.array([hsv_color[0]+20, hsv_color[1]+20, hsv_color[2]+20], dtype = np.uint8)

webcam = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cv2.namedWindow("frame")
cv2.setMouseCallback('frame',click)

while(1):
    ret, frame = webcam.read()
    frame = cv2.resize(frame,(640, 640), interpolation = cv2.INTER_CUBIC) #default res:480x640, showing IndexError while clicking on mouse
    frame = np.array(frame) # opencv expects a numpy array, otherwise the error: Expected Ptr<cv::UMat> for argument 'mat'
    frame = cv2.flip(frame,1) # mirror webcam video

    #uncomment the line below if you want to see the size of a frame
    #print('frame:', frame.shape) 
    cv2.imshow('frame', frame)
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #default masks for testing
    # Set range for green color and define mask 
    green_lower = np.array([25, 52, 72], np.uint8) 
    green_upper = np.array([102, 255, 255], np.uint8) 
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper) 
    # Set range for blue color and define mask 
    blue_lower = np.array([94, 80, 2], np.uint8) 
    blue_upper = np.array([120, 255, 255], np.uint8) 
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
    # Set range for red color and define mask 
    red_lower = np.array([136, 87, 111], np.uint8) 
    red_upper = np.array([180, 255, 255], np.uint8) 
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper) 

    #define my mask when you click
    my_mask = cv2.inRange(hsvFrame, lower, upper)
    my_mask = cv2.dilate(my_mask, kernal)

    #you can change my_mask on blue_mask/red_mask/green mask
    processed_frame = cv2.bitwise_and(frame, frame, mask = my_mask) #frame with your mask
    img3 = np.ubyte(0.5*processed_frame + 0.5*grayFrame[:, :, None]) #combine two image: gray and mask
    #your mask is showed in 'result' window
    cv2.imshow('result', img3)
    #press 'q' button to close all webcam windows
    if cv2.waitKey(10) & 0xFF == ord('q'): 
        webcam.release() 
        cv2.destroyAllWindows() 
        break

