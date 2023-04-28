#import all necassary packages
import cv2
from cv2 import CascadeClassifier

#cascade file
classifier=cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)

#while loop for capture of vedio in form of numerous frames of images
while True:

	ret,frame=cap.read()  #read the frame

	#convert frame to gray scale
	frame=cv2.cvtColor(frame,0)
	detections=classifier.detectMultiScale(frame,1.3,5) #this function detect the face from classifier
	if(len(detections)>0):
		(x,y,w,h)=detections[0]
		frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)   #make a rectangle arounf the detected face
	cv2.imshow('frame',frame)

	if cv2.waitKey(1) & 0xff ==ord('q'): #by pressing 'q' we can quit the program
		break
