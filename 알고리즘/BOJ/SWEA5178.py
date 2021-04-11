# 노드의 합


# 후위 순회
def postorder(idx):
    # 리프 노드가 전체 노드수보다 크면 -> 트리 크기를 초과
    if idx > N: 
        return 0
    
    # 완전 이진트리 특징 상 왼쪽은 노드 * 2
    # 오른쪽은 노드 * 2 + 1
    l = postorder(idx * 2)
    r = postorder(idx * 2 + 1)
    # 후위 순회이므로 왼쪽 오른쪽 끝난 후 값 계산해서 부모 노드에 넣어줌
    tree[idx] += l + r
    return tree[idx]

T = int(input())
for tc in range(1, T + 1):
    # 노드 수, 리프 노드 갯수, 출력할 번호 받기
    N, M, L = map(int, input().split())

    # 트리 초기화
    tree = [0] * (N + 1)

    # 리프 노드 번호, 데이터
    for _ in range(M):
        idx, val = map(int, input().split())
        # 트리 노드에 저장
        tree[idx] = val
    postorder(1)

    print('#%d' %(tc), tree[L])
