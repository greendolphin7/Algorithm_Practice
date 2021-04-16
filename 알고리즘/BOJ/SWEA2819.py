# 격자판의 숫자 이어붙이기

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def dfs(r, c, num):
    global result
    if len(num) == 7:
        result.append(num)
        return

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < 4 and 0 <= nc < 4:
            dfs(nr, nc, num + board[nr][nc])

T = int(input())
for tc in range(1, T + 1):
    board = list(list(input().split()) for _ in range(4))
    result = []
    for r in range(4):
        for c in range(4):
            dfs(r, c, board[r][c])
    result = set(result)

    print('#%d' %(tc), len(result))
