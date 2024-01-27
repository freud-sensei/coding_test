# 10진법 -> n진법 변환 함수
def radixchange(num, radix):
	if num == 0: return '0'
	nums = []
	while num:
		num, digit = divmod(num, radix)
		nums.append(str(digit))
	return ''.join(reversed(nums))

 
def solution(n):
	return int(radixchange(n, 3)[::-1], 3)