# 미로

def find_start(N):
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                return r, c

def boundary_check(r, c):
    return 0 <= r < N and 0 <= c < N and (maze[r][c] == 0 or maze[r][c] == 3)

def DFS(r, c):
    global ans

    if maze[r][c] == 3:
        ans = 1
        return

    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if boundary_check(nr, nc) and visited[nr][nc] == 0:
            DFS(nr, nc)

T = 10
for _ in range(1, T + 1):
    tc = int(input())
    N = 16
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = 0
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    start_r, start_c = find_start(N)
    DFS(start_r, start_c)

    print('#%d' % (tc), ans)
