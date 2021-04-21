# 최소 생산 비용

def DFS(idx, sum):
    global result

    if idx == N:
        if result > sum:
            result = sum
        return

    if result < sum:
        return

    for x in range(N):
        if visited[x] == False:
            visited[x] = True
            DFS(idx + 1, sum + data[idx][x])
            visited[x] = False

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(list(map(int, input().split())) for _ in range(N))
    visited = [0] * N
    result = 999999

    DFS(0, 0)
    print('#%d %d'%(tc, result))