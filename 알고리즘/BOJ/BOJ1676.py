# 팩토리얼 0의 개수

import sys
import math

def input():
    return sys.stdin.readline()

N = int(input())

def factorial(n):
    count = 0
    result = math.factorial(n)  # 팩토리얼 계산

    for index in range(-1, -1 * len(str(result)), -1):  # 계산 값을 문자열로 바꾼 다음 가장 뒷자리수 부터 시작해서 하나씩 앞자리로 반복
        if str(result)[index] == '0':  # 만약 그 자리값이 0이라면 
            count += 1                 # 전체 수에 더해주고
        else:
            break                      # 아니라면 for문에서 빠져나가자. 
    return count                       # 0 갯수 반환

print(factorial(N))