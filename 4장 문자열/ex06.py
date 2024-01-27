# 문자열을 배열로 만들기
def solution(s, n):
	s = list(s)

# 반복문으로 순회하며 문자에 숫자를 더하기
	for i in range(len(s)):
		if s[i] == ' ':
			continue
		corr = ord('A') if s[i].isupper() else ord('a')
		s[i] = chr((ord(s[i]) - corr + n) % 26 + corr)

# 다시 합치기
	return ''.join(s)