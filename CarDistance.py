import cv2
import winsound
import queue
from pytube import YouTube


video_url = 'https://www.youtube.com/watch?v=ifHdZ83n4E4'

vid = YouTube(video_url)
stream = vid.streams.get_highest_resolution()
stream.download(filename='car_pov.mp4')
# Initialize the camera (you may need to configure this based on your camera setup)
cap = cv2.VideoCapture('car_pov.mp4')  #  Youtube video





car_cascade = cv2.CascadeClassifier('haarcascade_cars.xml')

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    if frame is None:
        print("video finished")
        break
    # Get the dimensions of the frame
    height, width = frame.shape[:2]

    # Calculate the coordinates for the ROI (center of the frame)
    roi_x = width // 4 + width // 8
    roi_y = height // 4 + height // 8
    roi_width = width // 4
    roi_height = height // 4

    # Extract the ROI
    roi = frame[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

    # Draw a square frame around the ROI
    cv2.rectangle(frame, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 255, 0), 2)

    # Gray scale on for Car detection
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

    # Perform vehicle detection
    cars = car_cascade.detectMultiScale(gray_roi, scaleFactor=1.1, minNeighbors=3, minSize=(30, 30))

    # Draw rectangles around detected cars
    for (x, y, w, h) in cars:
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 0, 255), 2)

        car_size_percentage = (w * h) / (roi_width * roi_height) * 100

        if car_size_percentage >= 20:
            winsound.Beep(500, 100)
            print("Too close")

    # Display the frame with detected objects and distance information
    cv2.imshow('Distance Detection', frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
