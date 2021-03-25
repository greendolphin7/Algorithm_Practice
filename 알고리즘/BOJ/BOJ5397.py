# 키로거
import sys
from collections import deque

def input():
    return sys.stdin.readline()

T = int(input())

for tc in range(T):
        
    L = input()
    password = list()
    cursor = 0
    for i in L:
        if i == '<':
            if cursor <= 0:
                cursor = 0
                continue
            cursor -= 1
        elif i == '>':
            if cursor >= len(password) - 1:
                cursor = len(password) - 1
                continue
            cursor += 1
        elif i == '-':
            password.pop(cursor)
        else:
            password.insert(cursor, i)
            cursor += 1

    print(''.join(password))