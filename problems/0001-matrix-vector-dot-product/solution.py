import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:

	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if np.size(a, axis=1) != np.size(b, axis=0):
		return -1
	else:
		# Return a list where each element is the dot product of a row of 'a' with 'b'.
		return np.dot(a, b)
	