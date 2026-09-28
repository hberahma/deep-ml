def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	if mode == 'row':
		return [sum(e)/len(e) for e in matrix]
	else:
		return [sum(e)/len(e) for e in zip(*matrix)]