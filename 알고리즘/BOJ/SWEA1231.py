# 중위 순회

def inorder(v):
    global answer
    # 갈 수 없으면 돌아가
    if v == 0:
        return
    # 왼쪽 먼저 탐색
    inorder(L[v])
    # 단어 하나씩 더해주기
    answer += word[v - 1]
    # 오른쪽 탐색
    inorder(R[v])


T = 10
for tc in range(1, T + 1):
    # 정점 갯수 입력 받기
    V = int(input())

    # 왼쪽 트리 초기화
    L = [0] * (V + 1)
    # 오른쪽 트리 초기화
    R = [0] * (V + 1)
    # 부모
    P = [0] * (V + 1)

    word = []
    for i in range(V):
        # 정점 정보 입력
        arr = list(input().split())
        # 단어 리스트에 하나하나씩 알파벳 넣어주기
        word.append(arr[1])

        # 입력 갯수가 3개 이상인 경우 -> 왼쪽 자식 혹은 오른쪽 자식이 존재
        if len(arr) > 2:
            # 3번째 값부터 끝 값 까지 반복 돌면서
            for k in range(2, len(arr)):
                # 만약에 그 값이 0이라면 -> 왼쪽 자식 칸이 비어있다는 뜻
                if L[int(arr[0])] == 0:
                    # 왼쪽 자식과 연결
                    L[int(arr[0])] = int(arr[k])
                # 아니라면
                else:
                    # 오른쪽 자식과 연결
                    R[int(arr[0])] = int(arr[k])
                # 부모와 연결
                P[int(arr[k])] = int(arr[0])

    # 트리 모두 만들었으면 정답 초기화 한 후 순회 시작
    answer = ''
    inorder(1)
    print('#%d' % (tc), answer)
