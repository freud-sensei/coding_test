from collections import deque

def solution(skill, skill_trees):
	answer = 0

	for skills in skill_trees:
		skill_list = deque(skill[:])

		for s in skills:
			if s in skill and s != skill_list.popleft():
				break
		else: answer += 1
		# for-else 문: else문 뒤에는 반복문이 "끝까지 실행되었을 때 수행할 내용"이 들어간다. break되면 실행되지 않는다.
		# while-else 문: 마찬가지.