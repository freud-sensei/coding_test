def solution(record):
	answer = [] # 정답 배열
	actions = [] # 과정 배열
	user = {} # 유저 데이터

	for event in record:
		info = event.split()
		cmd, uid = info[0], info[1]
		if cmd in ("Enter", "Change"):
			nick = info[2]
			user[uid] = nick

		actions.append((cmd, uid))

	for action in actions:
		cmd, uid = action
		if cmd == "Enter":
			answer.append(f'{user[uid]}님이 들어왔습니다.')
		elif cmd == "Leave":
			answer.append(f'{user[uid]}님이 나갔습니다.')

	return answer