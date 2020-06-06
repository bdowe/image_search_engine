import numpy as numpy
import cv2
import imutils

class ColorDescriptor:
	def __init__(self, bins):
		self.bins = bins

	def describe(self, image):
		image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
		features = []

		h, w = image.shape[:2]
		cX, cY = int(w * 0.5), int(h * 0.5)