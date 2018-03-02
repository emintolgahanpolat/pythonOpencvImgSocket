import socket
import cv2
import numpy as np

cap = cv2.VideoCapture(0) 

HOST = 'localhost' # gonderilecek bilgisayarin ip adresi
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
    frame = cv2.resize(frame,None,fx=1, fy=1, interpolation = cv2.INTER_CUBIC) # resize fx ve fy orani 0-1 arasi deger alir
    height,width,layer=frame.shape
    print height,width,layer #burdaki degerler server.py ye yazilacak
    frameSend(frame)
   
    cv2.imshow('client',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cap.release()
cv2.destroyAllWindows()

