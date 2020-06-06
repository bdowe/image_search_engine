import numpy as numpy
import cv2
import imutils

class ColorDescriptor:
	def __init__(self, bins):
		self.bins = bins

	def describe(self, image):
		# convert image from BGR color space to HSV color space
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		features = []

		# extract height, width, and center coordinates from image
		h, w = image.shape[:2]
		cX, cY = int(w * 0.5), int(h * 0.5)

		# define regions for separating image into quadrants
		segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h), (0, cX, cY, h)]

		# define elliptical mask representing center of image
		axesX, axesY = int(w * 0.75) // 2, int(h * 0.75) // 2 
		ellipMask = np.zeros(image.shape[:2], dtype="uint8")
		cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)