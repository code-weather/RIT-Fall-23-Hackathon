"""
CarDistance

Description: Car Detector

Authors:
	Jessica Nguyen
    Jameson Wang
"""
import cv2
from pygame import mixer
from pytube import YouTube
import winsound
import threading


def play_beep():
    '''
    plays a winsound beep
    :return:
    '''
    winsound.Beep(500,200)

def CarDetector(video_url, mixer_use):
    '''
    Takes in a video url string, and checks to see if vehicles withing a region of
    interest(ROI) is greater than a certain percentage of the ROI, if so play a sound
    alerting user that they are driving too close to another car. Sound is played either
    using pygame mixer or using threads that call the function play_beep.
    :param video_url: URL of the Youtube video
    :param mixer_use: True if we pygame mixer, false use threads
    :return: none
    '''
    # get the youtube video url and download the car video
    vid = YouTube(video_url)
    stream = vid.streams.get_highest_resolution()
    stream.download(filename='car_pov.mp4')

    sound_playing = False
    threads_list = []
    if(not mixer_use):
        #create threads to play_beep
        for i in range(10):
            thread = threading.Thread(play_beep())
            threads_list.append(thread)
            thread.start()
    else:
        mixer.init()
        sound_file = 'mixkit-signal-alert-771.wav'
        mixer.music.load(sound_file)


    # Create video capture object
    cap = cv2.VideoCapture('car_pov.mp4')  # Youtube video

    #Create CascadeClassifier object used for car detection
    car_cascade = cv2.CascadeClassifier('haarcascade_cars.xml')

    #play the video
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

            #check to see it the distance of the car in ROI is too big
            if car_size_percentage >= 20:
                if (not mixer_use):
                    play_beep()

                if (mixer_use and not sound_playing ):
                    mixer.music.play()
                    sound_playing = True
                print("Too close")

            if(mixer_use and sound_playing):
                mixer.music.stop()
                sound_playing = False
        # Display the frame with detected objects and distance information
        cv2.imshow('Distance Detection', frame)

        # Exit the loop when the 'q' key is pressed or close window is clicked
        if cv2.waitKey(1) & 0xFF == ord('q') or \
                cv2.getWindowProperty('Distance Detection', cv2.WND_PROP_VISIBLE) < 1:
            break

    # Kill threads and release the camera and close all windows
    if (not mixer_use):
        for thrd in threads_list:
            thrd.join()

    cap.release()
    cv2.destroyAllWindows()



