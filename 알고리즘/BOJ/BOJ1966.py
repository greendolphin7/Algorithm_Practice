T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    que = list(map(int, input().split()))

    for idx, i in enumerate(que):
        que[idx] = (i, idx)

    count = 0
    while True:
        priority = que[0][0]
        if priority == max(que)[0]:
            print_num = que.pop(0)
            count += 1
            if print_num[1] == M:
                print(count)
                break
        else:
            que.append(que.pop(0))


### lambda 사용한 풀이
# T = int(input())

# for _ in range(T):
#     N, M = map(int, input().split())
#     que = list(map(int, input().split(' ')))

#     for idx, i in enumerate(que):
#         que[idx] = (i, idx)

#     count = 0
#     while True:
#         if que[0][0] == max(que, key=lambda x: x[0])[0]:
#             count += 1
#             if que[0][1] == M:
#                 print(count)
#                 break
#             else:
#                 que.pop(0)
#         else:
#             que.append(que.pop(0))