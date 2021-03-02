def perm(idx): # cur_sum: 지금까지 선택한 요소들 합
    global ans
    if idx == N:        # 순열 생성
        S = 0
        for i in range(N):
            S += arr[i][col[i]] # [0][col[0]], [1][col[1]]
        if S < ans: ans = S
        
    else:
        for i in range(N):
            if visit[i]: continue
            visit[i] = 1
            col[idx] = i
            perm(idx + 1)
            visit[i] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    col = [0] * N
    visit = [0] * N

    ans = 100000000000000000000000
    perm(0)
    print(ans)
