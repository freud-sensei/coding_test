def solution(rows, columns, queries):
	# 1씩 증가하는 행렬 만들기
	matrix = [[(i) * columns + (j + 1) for j in range(columns)] for i in range(rows)]

	# 회전해야 할 위치들의 값 받아오기
	result = []
	for x1, y1, x2, y2 in queries:
		result.append(rotate(x1 - 1, y1 - 1, x2 - 1, y2 - 1, matrix))

	return result

# 행렬을 시계방향으로 회전시키는 함수
def rotate(x1, y1, x2, y2, matrix):
	first = matrix[x1][y1]
	min_value = first

	# 왼쪽: 위로 1칸씩
	for k in range(x1, x2):
		matrix[k][y1] = matrix[k + 1][y1]
		min_value = min(min_value, matrix[k + 1][y1])

	# 아래: 왼쪽으로 1칸씩
	for k in range(y1, y2):
		matrix[x2][k] = matrix[x2][k + 1]
		min_value = min(min_value, matrix[x2][k + 1])

	# 오른쪽: 아래로 1칸씩
	for k in range(x2, x1, -1):
		matrix[k][y2] = matrix[k - 1][y2]
		min_value = min(min_value, matrix[k - 1][y2])

	# 위: 오른쪽으로 1칸씩
	for k in range(y2, y1 + 1, -1):
		matrix[x1][k] = matrix[x1][k - 1]
		min_value = min(min_value, matrix[x1][k - 1])

	matrix[x1][y1 + 1] = first
	return min_value
