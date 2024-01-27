from itertools import permutations
import re

# 순열을 이용해 연산자 3개의 우선순위 정하기
def solution(expression):
	operators = ["*", "+", "-"]
	answer = []

	for operator in permuations(operators):

		# 숫자와 연산자를 분리 -> 우선순위 기반 숫자 계산
		temp = re.split(r'([-+*])', expression) 
		for exp in operator:
			while exp in temp:
				idx = temp.index(exp)
				temp[idx-1] = str(calc(temp[idx-1:idx+2]))
				temp[idx] = temp[idx+1] = '' # 남은 빈 공간은 공백으로 교체
				temp = [i for i in temp if i] # 빈 공간은 제거

		answer.append(abs(int(temp[0])))

	return max(answer)

def calc(tokens):
	num1, exp, num2 = tokens
	if exp == '+': return int(num1) + int(num2)
	elif exp == '*': return int(num1) * int(num2)
	else: return int(num1) - int(num2)

