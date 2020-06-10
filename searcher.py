import numpy as np
import csv

class Searcher:
	def __init__(self, indexPath):
		self.indexPath = indexPath

	def search(self, queryFeatures, limit=10):
		results = {}

		