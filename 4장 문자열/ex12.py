# 10진수 -> 2진수 변화는 bin() 함수로 가능함

# 이진 변환의 횟수를 기록하는 변수
def solution(s):
	change, zero = 0, 0

	while s != "1":
		change += 1
		num = s.count("1") # 0이 몇개 있는지 = 전체에서 1의 개수를 빼기
		zero += len(s) - num
		s = bin(num)[2:] # 0b로 시작한다.

	return [change, zero]