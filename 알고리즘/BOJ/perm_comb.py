# arr = ['A', 'B', 'C', 'D']
arr = [1, 2, 3]
N = len(arr)

def perm_for():
    for i in range(N):
        arr[0], arr[i] = arr[i], arr[0]

        for j in range(1, N):
            arr[1], arr[j] = arr[j], arr[1]

            for k in range(2, N):
                arr[2], arr[k] = arr[k], arr[2]
                print(arr)
                arr[2], arr[k] = arr[k], arr[2]

            arr[1], arr[j] = arr[j], arr[1]
        
        arr[0], arr[i] = arr[i], arr[0]
# perm_for()


def perm(k):
    if k == N:
        print(arr)
    else:
        for i in range(k, N):
            arr[k], arr[i] = arr[i], arr[k]
            perm(k + 1)
            arr[k], arr[i] = arr[i], arr[k] 
# perm(0)



sel = [0] * N  # 뽑은 결과 적기
def perm_bit(idx, check):
    if idx == N:
        print(sel)
        return
    for j in range(N):
        if check & (1 << j):
            continue
        sel[idx] = arr[j]
        perm_bit(idx + 1, check | (1 << j))
# perm_bit(0, 0)


### 순열 재귀
check = [0] * N
sel = [0] * N
def perm_recur(idx):
    if idx == N:
        print(sel)
        # pass
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i] # 값을 써라
                check[i] = 1      # 사용했다는 표시
                perm_recur(idx+1)
                check[i] = 0      # 다음 반복문을 위한 원상복구
# perm_recur(0)


arr = ['A', 'B', 'C']
N = len(arr)
check = [0] * N
sel = [0] * N

def perm(idx):
    if idx == N:
        print(sel)
        return
    else:
        for i in range(N):
            if check[i] == 0:
                sel[idx] = arr[i]
                check[i] = 1
                perm(idx + 1)
                check[i] = 0
# perm(0)



R = 3

# for i in range(0, N):
#     for j in range(i + 1, N):
#         for k in range(j + 1, N):
#             print(arr[i], arr[j], arr[k])
# print('-' * 10)


arr = ['A', 'B', 'C']
N = len(arr)
choice = [0] * R

def comb(idx, start):
    if idx == R:
        print(choice)
    else:
        for i in range(start, N):
            choice[idx] = arr[i]
            comb(idx + 1, i + 1)
comb(0, 0)


R = 3
arr = ['A', 'B', 'C']
N = len(arr)
choice = [0] * R

def comb_prac(idx, start):
    if idx == R:
        print(choice)
    else:
        for i in range(start, N):
            choice[idx] = arr[i]
            comb_prac(idx + 1, i + 1)
comb_prac(0, 0)