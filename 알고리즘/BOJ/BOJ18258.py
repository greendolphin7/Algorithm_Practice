# 큐 2

import sys
from collections import deque


def input():
    return sys.stdin.readline()

n = int(input())

queue = deque([])  # 큐 생성
for i in range(n):
    command = input().split()           # 명령 한 줄 받기

    if command[0] == 'push':            # 명령이 push 라면
        queue.append(int(command[1]))   # push 뒤에 숫자 값을 넣는다.
    elif command[0] == 'pop':           # 명령이 pop 이라면
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())      # 리스트에서 하나 뽑아서 출력
    elif command[0] == 'size':
        print(len(queue))
    elif command[0] == 'empty':         # 큐가 비었는지 아닌지 판단
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':         # 큐의 맨 앞자리 수 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'back':          # 큐의 맨 뒷자리 수 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    
    