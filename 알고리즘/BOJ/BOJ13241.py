# 최소공배수

import sys

def input():
    return sys.stdin.readline()

a, b = input().split()
a = int(a)
b = int(b)

def factor_maker(n):
    factor_list = []
    for i in range(2, n+1):  

        while n % i == 0:
            factor_list.append(i)    
            n /= i

    return factor_list

a_factor = factor_maker(a)
b_factor = factor_maker(b)

common_factor_list = []
for factor in b_factor:
    if factor in a_factor:
        common_factor_list.append(factor)
    else:
        continue



answer = 1
for factor in common_factor_list:
    answer = answer * factor
print(answer)

answer = a * b // answer
print(answer, end='')
