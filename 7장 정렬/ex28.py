from functools import cmp_to_key

def solution(numbers):

	# 주어진 숫자 배열을 문자열로 교체
	numbers = list(map(str, numbers))

	# 정렬 기준에 맞게 내림차순으로 정렬
	numbers.sort(key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)), reverse=True)

	# 나온 결과값 합치기
	''.join(numbers)

	# 0에 대한 예외처리, 정답 반환
	return str(int(''.join(numbers)))

	# func() 함수는 두 개의 인수를 입력하여 첫 번째 인수를 기준으로 그 둘을 비교하고 작으면 음수, 같으면 0, 크면 양수를 반환하는 비교 함수이어야 한다.


# 다른 풀이
def solution(numbers):
	numbers = [str(x) for x in numbers]
	numbers.sort(key=lambda x: x * 3, reverse=True)
	result = ''.join(numbers)
	if '0' * len(numbers) == result: return '0'
	return result