def solution(phone_book):

	
	headers = dict()
	for phone_number in phone_book:

		# 자기 자신을 딕셔너리에 등록
		headers[phone_number] = 1

	# 문자열을 모두 쪼개, 한 글자씩 합쳐나가면서 나오는 결과를 등록
	
	for phone_number in phone_book:
		header = ''
		for number in phone_number:
			header += number
			if header in headers and header != phone_number:
				return False
	return True

# 이런 경우 set를 사용해도 된다.
