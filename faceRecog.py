import cv2
from cv2 import CascadeClassifier
classifier=cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)

while True:
	ret,frame=cap.read()
	frame=cv2.cvtColor(frame,0)
	detections=classifier.detectMultiScale(frame,1.3,5)
	if(len(detections)>0):
		(x,y,w,h)=detections[0]
		frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
	cv2.imshow('frame',frame)

	if cv2.waitKey(1) & 0xff ==ord('q'):
		break
