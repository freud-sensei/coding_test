from collections import defaultdict
from itertools import combinations
from bisect import bisect_left as left_bound

def solution(info, query):
	answer = []
	people = defaultdict(list) # 기본 value를 list로 처리

	for i in info:
		person = i.split()
		score = int(person.pop())
		people[''.join(person)].append(score) # '-'가 없는 버전

		for j in range(4):
			case = list(combinations(person, j)) # 0, 1, 2, 3
			for c in case:
				people[''.join(c)].append(score) # '-'가 있는 버전

	for i in people:
		people[i].sort()

	for i in query:
		key = i.split()
		score = int(key.pop())
		key = ''.join(key)
		key = key.replace('and', '').replace(' ', '').replace('-', '')
		answer.append(len(people[key]) - left_bound(people[key], score))

		return answer

