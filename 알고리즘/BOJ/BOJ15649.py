# N과 M (1)

N, M = map(int, input().split())

arr = list(i+1 for i in range(N))
sel = [0] * M
check = [0] * N

def perm(idx):
    if idx == M:
        print(' '.join(map(str, sel)))

    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i]
                check[i] = 1
                perm(idx + 1)
                check[i] = 0
perm(0)


# N, M = map(int, input().split())
# num = []
# visited = [0 for _ in range(N)]

# def perm(idx):
#     if idx == M:
#         print(" ".join(map(str, num)))
#         return
#     for i in range(N):
#         if visited[i] == 0:
#             num.append(i+1)

#             visited[i] = 1
#             perm(idx+1)

#             num.pop()
#             visited[i] = 0
# perm(0)
