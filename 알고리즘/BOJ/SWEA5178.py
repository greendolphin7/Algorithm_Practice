# 노드의 합

def postorder(idx):
    if idx > N: 
        return 0
    l = postorder(idx * 2)
    r = postorder(idx * 2 + 1)
    
    tree[idx] += l + r
    return tree[idx]

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)

    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val
    postorder(1)

    print('#%d' %(tc), tree[L])
