# 동철이의 일 분배

def cal_prob(num, local_optima):
    global answer

    if local_optima <= answer:
        return
    if num == N:
        answer = max(answer, local_optima)
        return

    for i in range(N):
        if visit[i] == True:
            continue
        visit[i] = True
        next_optima = local_optima * prob_list[i][num] * 0.01
        cal_prob(num + 1, next_optima)
        visit[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    prob_list = list(list(map(int, input().split())) for _ in range(N))

    visit = [False] * N
    answer = 0
    cal_prob(0, 1)
    print('#%d %.6f' %(tc, answer * 100))
