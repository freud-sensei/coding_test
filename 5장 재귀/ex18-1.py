# 직접 계산하기: 해당 글자가 해당 위치에 처음으로 등장하는 시점
# <해당 위치에서 나올 수 있는 단어의 개수>의 배수 + 1
def solution(word):

    preset = {'A': [1, 1, 1, 1, 1],
    'E': [782, 157, 32, 7, 2],
    'I': [1563, 313, 63, 13, 3],
    'O': [2344, 469, 94, 19, 4],
    'U': [3125, 625, 125, 25, 5]}

    answer = 0
    for idx, key in enumerate(word):
        answer += preset[key][idx]

    return answer

