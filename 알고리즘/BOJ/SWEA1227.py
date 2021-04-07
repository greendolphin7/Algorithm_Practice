# 미로2

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def find_start(N):
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                return r, c


def DFS():
    need_visit = []
    r, c = find_start(N)
    need_visit.append((r, c))
    visited[r][c] = 1

    while need_visit:
        node = need_visit.pop()
        r = node[0]
        c = node[1]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if visited[nr][nc] == 0 and 0 <= nr < N and 0 <= nc < N:
                if maze[nr][nc] == 3:
                    return 1
                if maze[nr][nc] == 0:
                    visited[nr][nc] = 1
                    need_visit.append((nr, nc))
    return 0


T = 10
for _ in range(1, T + 1):
    tc = int(input())
    N = 100
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = DFS()
    print('#%d' %(tc), ans)