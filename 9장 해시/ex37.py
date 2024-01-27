# 데이터를 딕셔너리에 정리하기
def solution(genres, plays):
	answer = []
	info = {}
	gens = {}

	for idx, (gen, play) in enumerate(zip(genres, plays)):
		if gen not in info:
			info[gen] = [(idx, play)]
		else:
			info[gen].append((idx, play))

		gens[gen] = gens.get(gen, 0) + play

	# 데이터를 정렬, 조건에 맞게 탐색
	for (gen, _) in sorted(gens.items(), key=lambda x:x[1], reverse=True):
		for (idx, _) in sorted(info[gen], key=lambda x:x[1], reverse=True):
			answer.append(idx)