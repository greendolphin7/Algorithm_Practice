# 팰린드롬?

import sys

def input():
    return sys.stdin.readline()    

# 접근 방법: Dynamic Programming으로 풀어야 시간 초과가 나지 않는다.
# for문, while문, 재귀 모두 써보았지만 결국 풀지 못하였다.
# DP 연습한다는 생각으로 다른사람의 코드를 참고해서 풀어보았다.


'''
예를 들어 N = 7 일 때, 모든 경우에 대해서 palindrome 결과값을 만들어서 저장해둬야 하기 때문에

아래와 같은 순서 쌍이 생기게 된다.
(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)
(1, 3), (2, 4), (3, 5), (4, 6), (5, 7)
(1, 4), (2, 5), (3, 6), (4, 7)
(1, 5), (2, 6), (3, 7)
(1, 6), (2, 7)
(1, 7)
'''

N = int(input())                         # 숫자 갯수
dp_list = [[0] * N for i in range(N)]    # 메모이제이션 기법을 사용하기 위해 숫자 갯수 제곱만큼 요소가 0인 리스트 생성 

num_list = list(map(int, input().split()))   # 전체 숫자 리스트 입력

for b in range(N):                       # 1 ~ N 까지 순서쌍을 만들어주기 위해 반복

    for start in range(N):               # 2중 for문을 만든 이유는 범위가 1 ~ 2 / 3 ~ 6 이런식으로 두가지 값이 필요하기 때문

        end = start + b                  # 끝점은 시작점에서 범위값을 더해준다.

        if end >= N:                     # 끝점이 전체 길이를 넘어가면 안된다.
            break                        # 따라서 끝점이 글자의 총 크기를 넘어버렸다면 for 문 종료하고 다음 범위로 이동

        if start == end:                 # 시작점과 끝점이 같다는 뜻은 단어가 하나 남았다는 것 -> palinedrome
            dp_list[start][end] = 1      # palinedrome 이라는 뜻인 1로 저장
            continue                     # 다음 쌍 찾기

        if start + 1 == end:             # 글자의 크기가 2개인 경우
            if num_list[start] == num_list[end]:    # 서로 값이 값다면
                dp_list[start][end] = 1             # palinedrome 저장
                continue                            # 다음 쌍 찾기

        if num_list[start] == num_list[end] and dp_list[start + 1][end - 1]:  # 시작과 끝점이 같고 그 다음 시작점과 끝점과의 결과가 일치하면 palindrome
            dp_list[start][end] = 1                                           # 그때의 시작점과 끝점은 palindrome

M = int(input())

for i in range(M):
    a, b = map(int, input().split())
    print(dp_list[a - 1][b - 1])

############################## 재귀 활용 ##############################
    # sys.setrecursionlimit(100000)
    # def palindrome(word):
    #     if len(word) < 2:
    #         return 1
        
    #     if word[0] != word[-1]:
    #         return 0
    #     else:
    #         return palindrome(word[1:-1])

############################## while문 활용 ##############################
    # def is_pal_while(word):
    # answer = 0
    # i = 0
    # while i <= len(word) // 2:
    #     if word[i] == word[len(word) - 1 - i]:
    #         answer = 1
    #     else:
    #          return 0
    #     i += 1
    # return answer