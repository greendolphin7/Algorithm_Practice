# 암호생성기

from collections import deque

for _ in range(10):
    tc = int(input())

    num_list = list(map(int, input().split()))
    queue = deque()

    for i in range(8):
        queue.append(num_list[i])

    while queue[-1] != 0:
        for i in range(1, 6):
            move_num = queue.popleft()
            move_num -= i
            if move_num <= 0:
                move_num = 0
            queue.append(move_num)
            if queue[-1] == 0:
                break

    ret = []
    for i in range(len(queue)):
        ret.append(str(queue[i]))

    print('#%d ' %(tc) + ' '.join(ret))