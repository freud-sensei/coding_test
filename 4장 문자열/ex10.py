def solution(s):
	answer = len(s)

	# 압축 가능한 길이만큼(전체의 1/2) 순회
	# 반복된 규칙을 확인하여 몇 번 반복되었는지, 반복된 문자열이 무엇인지 기록 후 반영
	for x in range(1, len(s) // 2 + 1):
		comp_len = 0
		curr = ''
		count = 1

		for i in range(0, len(s) + 1, x):
			new = s[i:i+x]
			if curr == new:
				count += 1
			else:
				comp_len += len(new)
				if count > 1:
					comp_len += len(str(count))
					count = 1
					curr = new

		# 압축 과정에서의 문자열 길이와 원래 문자열 길이 비교
		answer = min(answer, comp_len)

	return answer
