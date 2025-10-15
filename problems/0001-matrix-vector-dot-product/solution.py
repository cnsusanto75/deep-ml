def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	
	if len(a) == len(b):
		c = [0 for i in range(len(a[0]))]
		for i in range (len(c)):
			for j in range(len(b)):
				c[i] += a[i][j] * b[j]
		return c
	return -1
