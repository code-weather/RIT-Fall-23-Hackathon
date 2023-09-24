import cv2
import winsound  # Import the winsound module
import queue
from pytube import YouTube

video_url = 'https://www.youtube.com/watch?v=LD2qCy2tGh0'

vid = YouTube(video_url)
stream = vid.streams.get_highest_resolution()
stream.download(filename='car_pov.mp4')
# Initialize the camera (you may need to configure this based on your camera setup)
cap = cv2.VideoCapture('car_pov.mp4')  #  Youtube video

# Set the known width of the car in front (in meters)
known_car_width = 2.0  # Example: 2 meters

# Set the focal length of the camera (you'll need to calibrate this)
# Focal length = (width of the object in pixels * distance to the object) / known_car_width
focal_length = 1000.0  # Example: 1000 pixels

# Create an audio queue for alerts
audio_queue = queue.Queue()

car_cascade = cv2.CascadeClassifier()
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

    # Display the frame with the square frame around the ROI
    # Perform object detection and find the car in front
    # (You should use a pre-trained object detection model here)

    # Calculate the width of the car in pixels
    # (You can get this information from the object detection result)
    car_width_pixels = 100  # Example: 100 pixels

    # Calculate the distance to the car in front (in meters)
    distance = (known_car_width * focal_length) / car_width_pixels

    # Set a safe following distance threshold (in meters)
    safe_distance = 5.0  # Example: 5 meters

    # Check if the vehicle is too close to the car in front
    if distance < safe_distance:
        # Trigger an audio alert and add it to the audio queue
        audio_queue.put("alert.wav")  # Replace with your audio alert file

    # Play audio alerts from the queue
    while not audio_queue.empty():
        alert_sound = audio_queue.get()
        winsound.PlaySound(alert_sound, winsound.SND_FILENAME)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the frame with detected objects and distance information
    cv2.imshow('Distance Detection', gray_frame)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
