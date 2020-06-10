import numpy as np
import csv

class Searcher:
	def __init__(self, indexPath):
		self.indexPath = indexPath

	def search(self, queryFeatures, limit=10):
		results = {}

		with open(self.indexPath) as f:
			reader = csv.reader(f)

			for row in reader:
				# extract features from row in index csv file
				features = [float(x) for x in row[1:]] # skip 1st col, which contains image id

				# compute chi squared distance between query features and row features
				d = self.chi2_distance(features, queryFeatures)

				# store distance in results dictionary
				results[row[0]] = d

			f.close()

		# sort results by distance (smaller distance = more relevant)
		results = sorted([(v, k) for (k, v) in results.items()])

		return results[:limit]

	def chi2_distance(self, histA, histB, eps = 1e-10):
		'''
		Computes chi squared distance between two histograms.
		optional eps argument is included to prevent division by zero
		'''
		return 0.5 * np.sum([(a-b)**2 / (a+b+eps) for a, b in zip(histA, histB)])