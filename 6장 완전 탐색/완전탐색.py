# 재귀: 전체에서 n개를 뽑아서 만들기
def permutations(arr, n):
    result = []
    if n == 0: return [[]]

    for (i, num) in enumerate(arr):
        for j in permutations(arr[:i] + arr[i + 1:], n-1):
            result.append([num] + j)
    return result

    # ([0,1,2,3], 2) = ([0], ([1,2,3], 1)) + ([1], ([0,2,3], 1)) + ([2], ([0,1,3], 1)) + [3], ([0,1,2], 1))

from itertools import permutations
permutations([a, b, c, d], 3)

