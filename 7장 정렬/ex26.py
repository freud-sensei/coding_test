# 오름차순 정렬 풀이
def solutions(citations):
	citations.sort(reverse = True)
	for idx, citation in enumerate(citations):
		if idx >= citation:
			return idx

	return len(ciations)