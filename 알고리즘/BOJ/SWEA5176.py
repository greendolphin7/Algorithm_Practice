# 이진탐색
def make_tree(n):
    global count
    # 전체 노드 갯수를 넘어가지 않을 때까지
    if n <= N:
        # 왼쪽, 오른쪽 순서로 생성
        # 완전 이진 트리의 속성으로 인해
        # 오른쪽 노드는 현재 노드 수의 2배
        # 왼쪽 노드는 현재 노드 수의 2배 + 1 
        # 현재 count를 값으로 삽입
        # 값을 넣은 후에는 1씩 추가
        make_tree(n*2)
        arr[n] = count
        count += 1
        make_tree(n*2 + 1)


T = int(input())
for tc in range(1, T + 1):
    # 전체 노드 크기
    N = int(input())
    # 트리 초기화
    arr = [0 for i in range(N+1)]
    # 1부터 N+1까지 돌 예정. 현재 1로 초기화
    count = 1
    make_tree(1)
    print('#%d %d %d' %(tc, arr[1], arr[N//2]))