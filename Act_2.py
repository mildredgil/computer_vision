#!/usr/bin/env python
# coding: utf-8

# ## Homework 2

#    ### take photo and put text


import numpy as np
import cv2

matricula = 'A00820397'
nombre = 'Mildred Gil'
ventana = 'Photo nombre matricula'

video = cv2.VideoCapture(0)

while(True):
    ret, frame = video.read()
    if ret==True:
        cv2.imshow(ventana, frame)
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        #cv.putText(	img, text, org, fontFace, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]]	)
        cv2.putText(frame, nombre, (frame.shape[0] - 50, 20), font, 1, (255,255,255), 2,cv2.LINE_AA)
        cv2.putText(frame, matricula, (frame.shape[0] - 50, 50), font, 1, (255,255,255), 2,cv2.LINE_AA)
        
        if cv2.waitKey(1) & 0xFF == ord('s'): #save on pressing 's' 
            cv2.imwrite('photo.jpg',frame)
        
        if cv2.waitKey(20) & 0xFF == ord('q'): #close on pressing 'q'
            break

video.release()
cv2.destroyAllWindows()


# 
# ### Image Processing in OpenCV
#
import numpy as np
import cv2

video = cv2.VideoCapture(0)

# Choosing pixel
def px_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP: #get color on left btn pressing
        # Get color in RGB
        colorsB = frame[y,x,0]
        colorsG = frame[y,x,1]
        colorsR = frame[y,x,2]
 
        pix = np.uint8([[[colorsB,colorsG,colorsR ]]])
         
        #convert color to hsv
        pix_hsv = cv2.cvtColor(pix,cv2.COLOR_BGR2HSV)
        
        #define the lower and upper 
        lower_color = np.array([pix_hsv[0][0][0] - 15, 50, 50])
        upper_color = np.array([pix_hsv[0][0][0] + 15, 255, 255])
        
        #set mask 
        mask = cv2.inRange(hsv, lower_color, upper_color)
        kernel = np.ones((5,5),np.uint8)
        erosion = cv2.erode(mask,kernel,iterations = 1)
        cv2.imshow('mask', mask)
        
        #get final result
        res = cv2.bitwise_and(param,param, mask= mask)
        kernel = np.ones((5,5),np.uint8)
        erosion = cv2.erode(res,kernel,iterations = 1)
        
        cv2.imshow('res', res)

while(video.isOpened()):
    ret, frame = video.read()

    if ret == True:
        cv2.imshow('frame', frame)
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.setMouseCallback('frame', px_color, frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

video.release()
cv2.destroyAllWindows()