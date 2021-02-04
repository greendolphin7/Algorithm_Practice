# 덱

import sys

def input():
    return sys.stdin.readline()

n = int(input())

command_list_temp = []  # 명령 임시저장 리스트 // ['push 1', '', 'push 2', '', ...] 형태로 저장
for i in range(n):
    command_list_temp.extend(list(input().split('\n')))  # extend 사용해서 리스트안에 줄바꿈 단위로 넣기

command_list = []  # 실제 명령 모음 넣기 위한 리스트
for command in command_list_temp:
    if command != '':
        command_list.append(command)

queue = []  # 큐 생성
for command in command_list:
    if command[:10] == 'push_front':            # 명령이 push 라면
        queue.insert(0, int(command[10:]))    # push 뒤에 숫자 값을 넣는다.
    if command[:9] == 'push_back':
        queue.append(int(command[10:]))
    elif command == 'pop_front':                # 명령이 pop_front 이라면
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))           # 리스트에서 하나 뽑아서 출력
    elif command == 'pop_back':                # 명령이 pop_front 이라면
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop())           # 리스트에서 하나 뽑아서 출력
    elif command == 'size':
        print(len(queue))
    elif command == 'empty':              # 큐가 비었는지 아닌지 판단
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command == 'front':              # 큐의 맨 앞자리 수 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif command == 'back':               # 큐의 맨 뒷자리 수 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])