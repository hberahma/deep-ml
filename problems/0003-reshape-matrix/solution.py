import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
		return []
	st = []
	ans = []
	for row in a:
		for e in row:
			st.append(e)
			if len(st) == new_shape[1]:
				ans.append(st[::])
				st.clear()

	return ans