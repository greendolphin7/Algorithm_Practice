# 프린터 큐
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    que = list(map(int, input().split(' ')))

    for idx, i in enumerate(que):
        que[idx] = (i, idx)

    # que = [(i, idx) for idx, i in enumerate(que)]

    count = 0
    while True:
        if que[0][0] == max(que, key=lambda x: x[0])[0]:
            count += 1
            if que[0][1] == M:
                print(count)
                break
            else:
                que.pop(0)
        else:
            que.append(que.pop(0))