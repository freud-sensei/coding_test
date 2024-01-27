def solution(prices):
	# 주식 가격을 쌓아둘 스택
	stack = []
	answer = [0] * len(prices)

	# 상승세 여부 확인
	for i in range(len(prices)):
		while stack and prices[stack[-1]] > prices[i]:
			# while stack이 핵심이다 이거 안 넣으면 에러 뜬다
			past = stack.pop()
			answer[past] = i - past
		stack.append(i)

	# 남은 스택 비우기
	for i in stack:
		answer[i] = len(prices) - 1 - i

	return answer