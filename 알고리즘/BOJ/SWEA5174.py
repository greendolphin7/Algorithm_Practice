# subtree

def treeSize(v):
    global cnt
    if v == 0:
        return
    cnt += 1
    treeSize(L[v])
    treeSize(R[v])

T = int(input())

for tc in range(1, T + 1):
    E, N = map(int, input().split())
    arr = list(map(int, input().split()))
    V = E + 1
    L = [0] * (V + 1)
    R = [0] * (V + 1)
    P = [0] * (V + 1)

    for i in range(0, E * 2, 2):
        p, c = arr[i], arr[i + 1]
        # 왼쪽이 비어있으면 넣어줌
        if L[p] == 0:
            L[p] = c
        # 왼쪽 있으면 오른쪽으로 넣어줌
        else:
            R[p] = c
        # 들어온 놈 부모 적어주기
    cnt = 0
    treeSize(N)
    print('#%d' %(tc), cnt)