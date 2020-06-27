import Jetson.GPIO as GPIO
import time
import cv2

GPIO.setmode(GPIO.BOARD)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot Open Webcam!")

while True:
    ret, frame = cap.read()

    cv2.imshow('Input', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord('s'):
        break

cap.release()
cv2.destroyAllWindows()
