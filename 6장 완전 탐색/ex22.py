from itertools import permutations

# 소수인지 판별
def checkprime(n):
	if n < 2:
		return False

	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False

	return True

# 모든 숫자 찾기
def solution(numbers):
	num = []
	for i in range(1, len(numbers) + 1):
		num.append(list(permutations(numbers, i))) # permutations는 tuple을 반환한다
	num = [int(''.join(y)) for x in num for y in x] # flatten

	for i in num:
		if checkPrime(i):
			answer.append(i)

	return len(set(answer))
