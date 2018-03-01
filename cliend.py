import socket
import cv2
import numpy as np

cap = cv2.VideoCapture(0) 

HOST = 'localhost'
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 4096

def frameSend(frame):
    d=frame.flatten()
    s=d.tostring()

    print len(s)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    client.send(s)

    client.close()


while(True):

    ret, frame = cap.read()
    frameSend(frame)
   
    cv2.imshow('client',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()

