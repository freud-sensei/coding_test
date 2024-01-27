# 주어진 원래 아이디에서 제재 아이디 개수만큼 뽑는 순열을 만들고
# 이 순열이 제재 아이디 규칙과 일치하는지 확인

import re

# 제재 아이디 규칙을 정규표현식에 맞춰 수정
def solution(user_id, banned_id):
	answer = set()
	banned = ' '.join(banned_id).replace('*', '.')

# 모든 순열과 규칙을 비교
	for i in permutations(user_id, len(banned_id)):
		if re.fullmatch(banned, ' '.join(i)):
			answer.add(''.join(sorted(i)))

	return len(answer)