# 스택

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

queue = []  # 스택 생성
for command in command_list:
    if command[0:4] == 'push':            # 명령이 push 라면
        queue.insert(0, int(command[5:])) # push 앞에 숫자 값을 넣는다.
    elif command == 'pop':                # 명령이 pop 이라면
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))           # 리스트 앞에서 하나 뽑아서 출력
    elif command == 'size':               # 스택의 갯수 리턴
        print(len(queue))
    elif command == 'empty':              # 스택이 비었는지 아닌지 판단
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command == 'top':                # 스택의 맨 앞자리 수 출력
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])