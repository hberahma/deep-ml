def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	# Return the element-wise sum of vectors 'a' and 'b'.
	# If vectors have different lengths, return -1.
	n, m = len(a), len(b)
	if n != m:
		return -1
	return [a[i] + b[i] for i in range(n)]