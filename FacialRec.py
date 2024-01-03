"""
FacialRec

Description: Eye dector

Authors:
	Jessica Nguyen
	Jameson Wang
	...
"""
import cv2
import time
import os  # Import os for Mac


def facialRec():
    '''
    Detects eyes from a webcam video. Plays beeping noise if eyes are not
    detected
    :return: none
    '''
    # Create CascadeClassifier Objects for facial and eye recognition
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    # Create a VideoCapture object using webcam
    cap = cv2.VideoCapture(0)

    # keeps track of the time
    last_detection_time = time.time()

    while True:
        _, img = cap.read()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = img[y:y + h, x:x + w]
            eyes = eye_cascade.detectMultiScale(roi_gray)

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)
            # if eyes are detected, update the last-detected-time
            if len(eyes) > 0:
                last_detection_time = time.time()
        # if current time is greater than last_detection time by 1 second, alert driver
        if ((time.time() - last_detection_time) > 1.0):
            os.system('say "Eyes not detected"')  # Use the 'say' command for alert
            print("Eyes not detected")

        cv2.imshow('img', img)

        k = cv2.waitKey(30) & 0xff
        if k == 27 or cv2.getWindowProperty('img', cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()