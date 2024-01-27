
def solution(n, times):
	answer = 0
	left, right = 1, min(times) * n

	while left <= right:
		mid = (left + right) // 2
		people = 0
		test = []

		# 주어진 임의의 시간에 최대 몇 명을 심사할 수 있는지
		for time in times:
			people += mid // times
			if people >= n: break

		if people >= n:
			answer = mid
			right = mid - 1

		elif people < n:
			left = mid + 1

	return answer