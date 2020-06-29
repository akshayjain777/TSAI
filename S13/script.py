# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 13:24:59 2020

@author: admin
"""

import cv2 

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("video1.mp4", 10, 20, targetname="test.mp4")

# Function to extract frames 
def FrameCapture(path): 
	
	# Path to video file 
	vidObj = cv2.VideoCapture(path) 

	# Used as counter variable 
	count = 0

	# checks whether frames were extracted 
	success = 1

	while success: 

		# vidObj object calls read 
		# function extract frames 
		success, image = vidObj.read() 

		# Saves the frames with frame-count 
		cv2.imwrite("frame%d.jpg" % count, image) 

		count += 1

# Driver Code 
if __name__ == '__main__': 

	# Calling the function 
	FrameCapture("video1.mp4") 
