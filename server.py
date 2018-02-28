import socket
import cv2
import numpy

HOST = ''
PORT = 9876
ADDR = (HOST,PORT)
BUFSIZE = 4096

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv.bind(ADDR)
serv.listen(5)

print 'listening ...'

while True:
  conn, addr = serv.accept()
  print 'client connected ... ', addr

  s=""
  while True:
    data = conn.recv(BUFSIZE)
    if not data: break
    s+=data
  frame = numpy.fromstring (s,dtype=numpy.uint8)
  frame = frame.reshape (480,640,3)
  cv2.imshow('server',frame)
  s=""

  if cv2.waitKey(1) & 0xFF == ord ('q'):
    break
  conn.close()
  print 'client disconnected'


