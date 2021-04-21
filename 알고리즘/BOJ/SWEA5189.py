# 전자카트

def dfs(next, val):
    global answer, count

    if val >= answer:
        return
    
    if count == N:
        val += rooms[next][0]
        answer = min(answer, val)
        return

    for i in range(1, N):
        if visited[i]:
            continue
        visited[i] = 1
        count += 1
        dfs(i, val + rooms[next][i])
        count -= 1
        visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    answer = 9999
    count = 1
    sub_result = rooms[0][0]
    visited = [0] * N
    dfs(0, 0)
    print('#%d' %(tc), answer)
    