def solution(stones, k):
	# 처음은 0, 끝은 디딤돌 중 가장 큰 숫자
	start, end = 0, max(stones)
	answer = 0

	while start <= end:
		mid = (start + end) // 2
		if available(mid, stones, k):
			start = mid + 1
			answer = max(answer, mid)
		else: end = mid - 1


# 현재 주어진 인원 수만큼 다리를 건널 수 있는가?
def available(n, stones, k):
	skip = 0
	for s in stones:
		if stone < n:
			skip += 1
			if skip >= k:
				return False
		else: skip = 0
	return True
