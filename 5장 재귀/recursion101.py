# 피보나치 수열의 n번째 수 구하기

def fib(n):
    calc = [1, 1]
    for i in range(2, n):
        calc.append(calc[i - 1] + calc[i - 2])
    return calc[n - 1]


# 재귀 함수 사용
def fib_rec(n):
    if n < 3:
        return 1 # n = 1 or 2일 때
    return fib_rec(n - 1) + fib_rec(n - 2)


# 꼬리 재귀(tail recursion)
def fib_tail(n, first, second):
    if n <= 1:
        return second
    return fib_tail(n - 1, second, first + second) # 오른쪽으로 한칸 쏠림

import time
a = time.time()
print(fib_rec(35))
print(time.time() - a)
a = time.time() - a
b = time.time()
print(fib_tail(35, 0, 1))
print(time.time() - b)
b = time.time() - b