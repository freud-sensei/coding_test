def solution(s):
	answer = []

	# 첫 중괄호를 제거하고 분리 기준을 설정하기
	data = s[2:-2].split("},{")

	# 튜플의 조건에 맞춰 쪼개진 문자열을 길이에 맞춰 정렬하
	data = sorted(data, key=lambda x: len(x))

	# 쪼갠 문자열을 ',' 기준으로 쪼개진 숫자가 있는 문자 찾기

	for item in data:
		item = list(map(int, item.split(',')))
		for value in item:
			if value not in answer:
				answer.append(value)

	return answer