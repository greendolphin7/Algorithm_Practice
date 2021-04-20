# 백트래킹 - 전기 버스 2

def DFS(num):
    global count, result

    if num >= N:
        if result > count:
            result = count
        return

    # 가지치기
    if result < count:
        return

    for i in range(num + data[num], num, -1):
        count += 1
        DFS(i)
        count -= 1


T = int(input())
for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    N = data[0]
    result = 99999
    count = 0

    DFS(1)

    print('#%d' %(tc), result-1)