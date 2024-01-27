def solution(participant, completion):
	answer = {}
	for i in participant:
		answer[i] = answer.get(i, 0) + 1
		# 만약 i가 key로 없으면 default 값인 0을 return
	for j in completion:
		answer[j] -= 1
	for k in answer:
		if answer[k]:
			return k

# 해시 함수를 이용
def solution(participant, completion):
	value = 0
	answer = {}
	for p in participant:
		answer[hash(p)] = p		
		value += int(hash(p))
	for c in completion:
		value -= hash(c)
	return answer[value]