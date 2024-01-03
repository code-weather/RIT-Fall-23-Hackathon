# **Car Distance and Eye Tracker**

This project combines a **Car Detector** and an **Eye Tracker** to enhance driving safety. It alerts drivers when they are too close to other vehicles and when their eyes are not detected on the road.

## **Features**

- **Car Distance Detection**: Detects vehicles within a defined region of interest in a video feed, alerting the driver if they are too close to another car.
- **Eye Tracking**: Monitors the driver's eyes using a webcam. If the eyes are not detected for more than a second, it alerts the driver.

## **Prerequisites**

Before running this project, ensure you have the following installed:
- Python 3
- OpenCV-Python
- Pygame (for sound functionality)
- Pytube (for downloading YouTube videos)

## **Installation**

Clone the repository to your local machine:

git clone https://github.com/code-weather/RIT-Fall-23-Hackathon.git

Install the required Python packages:
pip install opencv-python
pip install pygame
pip install pytube

## **Usage**

Run the main script to start the application:
python main.py

The program will prompt you to choose between Car Detection (C), Eye Tracking (F), or to Quit (Q).

### **Car Detector**

Enter 'C' to use the Car Detector. You will need to provide a YouTube video URL for the car footage.

### **Eye Tracker**

Enter 'F' to use the Eye Tracker. Ensure your webcam is connected and functioning.