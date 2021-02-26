# 오목 판정

def check(board, N):
    
    for r in range(N):
        for c in range(N):
            if board[r][c] == 'o':
                for i in range(8):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    count = 0
                    for j in range(4):
                        if 0 <= nr < N and 0 <= nc < N:
                            if board[nr][nc] == 'o':
                                count += 1
                            else:
                                count = 0
                                break
                            nr += dr[i]
                            nc += dc[i]
                        else:
                            break
                    if count >= 4:
                        return True

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    board = list(list(input()) for _ in range(N))

    dr = [-1, 1, 0, 0 ,-1, 1, 1, -1]
    dc = [0, 0, -1, 1, 1, 1, -1, -1]


    if check(board, N) == True:
        answer = 'YES'
    else:
        answer = 'NO'
    print('#%s ' %(tc) + answer)
