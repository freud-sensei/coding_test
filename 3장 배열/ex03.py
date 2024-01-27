def solution(n):
	# n x n 2차원 배열을 생성한다.
	snail = [[0] * i for i in range(1, n + 1)]

	# 나선형 형태로 배열을 채워나간다.
	dr = [1, 0, -1]
	dc = [0, 1, -1]
	x, y, angle = 0, 0, 0
	count = 1
	size = n * (n + 1) // 2

	while count <= size:
		snail[r][c] = count
		new_r = r + dr[angle]
		new_c = c + dc[angle]
		count += 1

		if 0 <= new_r < n and 0 <= new_c <= new_r and snail[new_r][new_c] == 0:
			r, c = new_r, new_c
		else:
			angle = (angle + 1) % 3
			r += dr[angle]
			c += dc[angle]

	return [i for j in snail for i in j] 