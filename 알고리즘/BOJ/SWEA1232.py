# 사칙 연산

def postorder(v):
    if len(tree[v]) > 2:
        operator, left, right = tree[v][1], postorder(int(tree[v][2])), postorder(int(tree[v][3]))

        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        else:
            return left / right
    else:
        return int(tree[v][1])


T = 10
for tc in range(1, T + 1):
    N = int(input())

    tree = [0] * (N + 1)

    for i in range(1, N + 1):
        lst = list(input().split())
        tree[i] = lst
    result = int(postorder(1))

    print('#%d' %(tc), result)