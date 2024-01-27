# 정렬을 2번 하기
def solution(strings, n):
	return sorted(sorted(strings), key=lambda x: x[n])

# 키 값을 바꾸기
def solution(strings, n):
	return sorted(strings, key=lambda x: x[n] + x)

# 튜플로도 구현할 수 있다
def solution(strings, n):
	return sorted(strings, key=lambda x: (x[n], x))