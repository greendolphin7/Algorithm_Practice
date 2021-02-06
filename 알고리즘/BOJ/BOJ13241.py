# 최소공배수

import sys

def input():
    return sys.stdin.readline()

a, b = input().split()
a = int(a)
b = int(b)

# 접근 방식: 최대 공배수 = 두 수의 곱 / 최대 공약수
# 먼저 최대공약수를 구한 후, 정답을 출력한다.

def gcd(x, y):              # 최대공약수를 구하기 위한 함수
    while y != 0:           # y가 0이 아니라면
        x, y = y, x % y     # x를 y와 바꾸고 y는 x의 나머지로 바꿔준다.
    return x

answer = a * b // gcd(a, b)
print(answer, end='')
