def solution(s):
	# 딕셔너리의 중복 검사 시간은 O(1)
	answer = {}

	# 첫 중괄호를 제거하고 분리 기준을 설정하기
	# 튜플의 조건에 맞춰 쪼개진 문자열을 길이에 맞춰 정렬하
	data = sorted(s[2:-2].split("},{"), key=len)

	# 쪼갠 문자열을 ',' 기준으로 쪼개진 숫자가 있는 문자 찾기

	for item in data:
		item = item.split(',')
		for i in item:
			if number not in answer:
				answer[number] = 1

	# 리스트를 선언할 때 값으로 딕셔너리를 넣으면 키값만이 배열 인자로 들어간다.
	# 후속 조치 필요 없음.
	return list(answer)