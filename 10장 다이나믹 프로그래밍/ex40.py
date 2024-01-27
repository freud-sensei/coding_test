def solution(triangle):

	# 계산 결과를 계속 쌓을 배열 생성
	# 0을 붙이면 그 다음 행 맨 왼쪽, 맨 오른쪽 계산할 때 오류가 발생하지 않음
	dp = [[0, *t, 0] for t in triangle]

	# 맨 꼭대기부터 시작해 하나씩 내려가면서 계산
	# dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])
	for i in range(1, len(triangle)):
		for j in range(1, i + 2):
			dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

	return max(dp[-1])


# 아래에서 위로 올라오는 식으로 풀이
def solution(triangle):
	height = len(triangle) - 1 # 4

	while height > 0:
		for i in range(height):
			triangle[height - 1][i] += max(triangle[height][i], triangle[height][i + 1])
		height -= 1

	return triangle[0][0]