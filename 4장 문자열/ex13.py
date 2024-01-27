def solution(new_id):
	answer = new_id.lower()

	filtered = []
	for c in answer:
		if c.isalpha() or c.isdigit() or c in ('-', '_', '.'):
			filtered.append(c)
	answer = ''.join(filtered)

	while '..' in answer:
		answer = answer.replace('..', '.')
		# replace는 가장 먼저 발견된 것만 수정

	answer = answer.strip('.') # 양옆으로 '.'를 제거

	if answer == '':
		answer = 'a'

	if len(answer) > 15: answer = answer[:15]
	if answer[-1] == '.': answer = answer[:-1]

	while len(answer) < 3:
		answer += answer[-1]

	return answer