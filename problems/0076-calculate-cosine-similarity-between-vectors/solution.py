import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	# Implement your code here
	return sum(v1[i]*v2[i] for i in range(len(v1))) / np.sqrt((sum(v1[i]*v1[i] for i in range(len(v1))) * sum(v2[i]*v2[i] for i in range(len(v1)))))