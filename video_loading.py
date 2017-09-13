import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
out = cv2.VideoWriter('output.m4v', fourcc, 20.0, (640,480))

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640,480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Need only 8 bits
        break
cap.release()
out.release()
cv2.destroyAllWindows()
