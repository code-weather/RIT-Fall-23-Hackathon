"""
Main Script

Description: Runs Eye Tracker and Car detector

=======
Authors:
	Jessica Nguyen
	Meghan Black
	Jameson Wang

"""

import CarDistance
import FacialRec


def main():
	'''
	Asks for user input on whether they would like to use the Car
	Detector or the facial Recgonition software. Loop until they
	enter Q.
	:return: none
	'''
	video_url = 'https://www.youtube.com/watch?v=ifHdZ83n4E4'
	while(True):
		x = input("Enter C for Car Dection, F for EyeTracker, or Q to quit\t").strip().upper()
		if (x == "C"):
			CarDistance.CarDetector(video_url,False)
		elif (x == "F"):
			FacialRec.facialRec()
		elif (x == "Q"):
			break
		else:
			print("Not an option")


if __name__ == '__main__':
	main()
# >>>>>>> refs/remotes/origin/main
