# 길찾기

def dfs(v):
    visited[v] = True
    for w in range(1, V + 1):
        if arr[v][w] == 1 and visited[w] == 0:
            dfs(w)


for _ in range(10):
    tc, E = map(int, input().split())
    V = 100
    road_list = list(map(int, input().split()))
    arr = [[0] * (V + 1) for _ in range(V + 1)]

    for i in range(0, E * 2, 2):
        s, e = road_list[i], road_list[i + 1]
        arr[s][e] = 1

    visited = [0] * (V + 1)

    dfs(0)
    if visited[99] == True:
        answer = 1
    else:
        answer = 0
    print('#%d' %(tc), answer)