from itertools import combinations
def solution(numbers):
	selects = list(combinations(numbers, 2))
	answer = set()
	for s in selects:
		(a, b) = s
		answer.add(a + b)

	return sorted(answer)