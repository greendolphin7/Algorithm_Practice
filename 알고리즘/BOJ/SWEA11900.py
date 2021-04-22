# 최소 신장 트리

def get_parent(x):
    if node[x] != x:
        node[x] = get_parent(node[x])
    return node[x]


def union_node(x, y):
    # 노드 합치기
    a = get_parent(x)
    b = get_parent(y)
    if a > b:
        node[a] = b
    else:
        node[b] = a


def find(x, y):
    return get_parent(x) == get_parent(y)


T = int(input())
for tc in range(1, T + 1):
    answer = 0
    V, E = map(int, input().split())

    node = list(i for i in range(V + 1))
    edge = list(list(map(int, input().split())) for _ in range(E))
    edge.sort(key=lambda x: -x[2])

    while edge:
        n1, n2, w = edge.pop()
        if find(n1, n2) == False:
            union_node(n1, n2)
            answer += w

    print('#%d' %(tc), answer)
