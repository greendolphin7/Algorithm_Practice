# N과 M (1)

# N, M = map(int, input().split())

# for i in range(1, N + 1):
#     for j in range(1, M + 1):
#         print(i, j)

# N = 3
# arr = 'ABC'
# order = [0] * N    # 생성한 순열을 저장

# for i in range(N): # 첫번째 위치의 요소(or 인덱스)를 선택
#        order[0] = arr[i]

#        for j in range(N): # 두번째 위치의 요소를 선택
#               order[1] = arr[j]

#               for k in range(N): #  세번째 위치의 요소를 선택
#                      order[2] [k]= arr

#                      print(*order)



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

# from itertools import permutations

# N, M = map(int, input().split())
# P = permutations(range(1, N+1), M)
# for i in P:
#     print(' '.join(map(str, i)))

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