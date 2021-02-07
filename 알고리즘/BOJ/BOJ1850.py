# 최대 공약수

import sys

def input():
    return sys.stdin.readline()

a, b = input().split()
a = int(a)
b = int(b)

# 유클리드 호제법이라는 방식으로 구한다.
# 유클리드 호제법이란, 2개의 자연수 a, b(a>b)에 대해서 a를 b로 나눈 나머지를 r이라 하면, 
# a와 b의 최대공약수는 b와 r의 최대공약수와 같다는 성질을 이용한다.

def gcd(x, y):              # 최대공약수를 구하기 위한 함수 (x가 y보다 커야 한다.)
    if x < y:
        x, y = y, x
    while y != 0:           # y가 0이 아니라면
        x, y = y, x % y     # x를 나누는 수로 바꾸고 y는 x를 나누었을 때의 나머지로 바꿔준다.
                            # 이 과정을 반복하여 나머지가 0이 된다면  x가 최대공약수가 된다.
    return x

answer = gcd(a, b)
answer = '1' * answer

print(answer, end='')
