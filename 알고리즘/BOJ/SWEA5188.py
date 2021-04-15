# 최소합

dr = [0, 1]
dc = [1, 0]

def dfs(start_node):
    global sub_result, answer
    r, c = start_node

    if sub_result > answer:
        return
    if r == N - 1 and c == N - 1:
        answer = sub_result
        return

    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < N and (nr, nc) not in visited:
            visited.append((nr, nc))
            sub_result += board[nr][nc]
            dfs((nr, nc))
            visited.remove((nr, nc))
            sub_result -= board[nr][nc]
    

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = list(list(map(int, input().split())) for _ in range(N))
    visited = []
    start_node = (0, 0)
    sub_result, answer = board[0][0], 9999
    dfs(start_node)
    print('#%d' %(tc), answer)