# 재귀 이용
sys.setrecursionlimit(200000) # 이걸 설정 안 하면 뻗을 것임.

def solution(n):
	answer = [0] * (n)
	answer[0] = answer[1] = 1
	fibo(n - 1, answer)
	return answer[-1] % 1234567

def fibo(n, answer):
	if n < 2:
		return 1
	if answer[n] == 0:
		answer[n] = fibo(n-1, answer) + fibo(n-2, answer)
	return answer[n]	

# 반복문 이용
def solution(n):
	a, b = 0, 1
	for i in range(n):
		a, b = b, a + b
	return a % 1234567