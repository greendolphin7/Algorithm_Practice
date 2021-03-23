# 섬의 개수
import sys
sys.setrecursionlimit(10**7)


dr = [-1, 0, 1, 0, -1, 1, 1, -1]
dc = [0, 1, 0, -1, 1, 1, -1, -1]

def DFS(r, c):
    land[r][c] = 2

    for i in range(8):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < h and 0 <= nc < w:
            if land[nr][nc] == 1:
                DFS(nr, nc)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    land = [list(map(int, input().split())) for _ in range(h)]
    
    count = 0
    for r in range(h):
        for c in range(w):
            if land[r][c] == 1:
                DFS(r, c)
                count += 1

    print(count)