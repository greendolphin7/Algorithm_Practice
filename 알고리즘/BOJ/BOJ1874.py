# 스택 수열

N = int(input())
stack = []
answer = []
count = 1

for i in range(1, N + 1):  # 1 ~ N 까지 반복해서 넣기
    current_num = int(input())  # 현재 수열에 넣어야 하는 숫자
    while count <= current_num: # 현재 숫자에 도달할 때까지는 계속 더해주어야 한다.
        stack.append(count)     # 스택에 숫자 넣어주고
        count += 1              # 하나씩 증가시키며 넣어준다.
        answer.append('+')
    if stack[-1] == current_num:  # 계속 더해주고 넣어야하는 숫자랑 스택 마지막이랑 같으면 
        stack.pop()               # 스택에서 제거해준다.
        answer.append('-')      
    else:
        print('NO')               # 만약에 그게 일치하지 않는다면 수열이 성립하지 않는다는 뜻!
        exit(0)                   # 스택이 오름차순으로 되지 않는다는 것이다.
print('\n'.join(answer))