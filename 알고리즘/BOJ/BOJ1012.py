# 유기농 배추

import sys
sys.setrecursionlimit(10**7)

def DFS(row, col):
    farm[row][col] = 2
    for d in range(4):
        nr = row + dr[d]
        nc = col + dc[d]
        
        if 0 <= nr < M and 0 <= nc < N:
            if farm[nr][nc] == 1:
                DFS(nr, nc)


for tc in range(int(input())):
    N, M, K = map(int, input().split())

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    farm = [[0] * N for _ in range(M)]
    
    for i in range(K):
        c, r = map(int, input().split())
        farm[r][c] = 1

    count = 0
    for row in range(M):
        for col in range(N):
            if farm[row][col] == 1:
                DFS(row, col)
                count += 1
    print(count)