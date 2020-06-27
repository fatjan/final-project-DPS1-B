import Jetson.GPIO as GPIO
import time
import cv2
import numpy as np
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
import tensorflow as tf

# Set GPIO
GPIO.setmode(GPIO.BOARD)

# Input Model Name
h5name = input('\n\nInput H5 File Name: ')
if h5name[-3:] != '.h5':
    h5name = h5name + '.h5'
try:
    model = tf.keras.models.load_model(h5name)
except Exception as e:
    print('\n\nModel not found!!!')
    print(e)
    exit()

# Open Webcam Stream
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("\n\nCannot open webcam!!!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("\n\nError receiving frame!!!")
        break
    #print(frame.shape)

    frame = cv2.rectangle(frame,
                          (192 - 2, 112 - 2),  # Start Coordinate
                          (448 + 2, 368 + 2),  # End Coordinate
                          (0, 255, 0),  # Color in BGR
                          1)  # Thickness
    #frame = cv2.putText(frame,
    #                    '~ guntingbatukertas ~',  # Text
    #                    (140, 27),  # Origin (bottom-left corner of the text)
    #                    cv2.FONT_HERSHEY_SIMPLEX,  # Font
    #                    1,  # Font Scale
    #                    (0, 255, 0),  # Color in BGR
    #                    1,  # Thickness
    #                    cv2.LINE_AA)  # Line Type (optional)
    crop = cv2.cvtColor(frame[112:368, 192:448], cv2.COLOR_BGR2RGB)
    #crop = cv2.resize(crop, (150, 150))
    #print(crop.shape)
    x = crop/255.0
    x = np.expand_dims(x, axis=0)
    images = np.vstack([x])

    cv2.imshow('Input', frame)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord('s'):
        break
    elif key == ord('p'):
        prediction = model.predict(images.astype(np.float32), batch_size=10)
        print(prediction)

cap.release()
cv2.destroyAllWindows()
