# 쉽게 푸는 문제

a, b = map(int, input().split())


# 접근 방법: 1 ~ b까지의 수열에서 1 ~ a-1 까지의 수열의 합을 빼면 된다.
# n을 집어 넣었을 때 1 ~ n 까지의 수열의 합 구하는 함수
def sum_number(n):
    answer = 0
    i = 1
    while n > 0:                    
        for repeat in range(i):         # 더해주는 값을 반복해서 정답에 더하기 위한 for문
            answer += i                 # 최종 수열합은 더해주고
            n -= 1                      # 총 반복해야하는 값을 1 빼준다.
            if n <= 0:                  # 만약 차례차례 모두 더했다면 
                return answer           # 정답을 리턴해준다.
        i += 1                          # 정답에 더해야 하는 값을 하나씩 더해준다.
    return answer                       # 이 리턴이 있는 이유는 A, B가 같은 수인 경우가 있기 때문

print(sum_number(b)-sum_number(a-1))



### 풀고난 후 다른 사람의 더 좋은 풀이

# A, B = map(int, input().split())

# a = []
# a.append(0)               # 리스트를 만들어주고
# for i in range(1000):
#     for j in range(i):    # 범위는 1 ~ 1000까지이기 때문에 수열을 미리 다 만들어준다.
#         a.append(i)

# sum = 0
# for i in range(A, B+1):   # A ~ B 까지의 리스트 요소들을 더해준다. 
#     sum += a[i]
# print(sum)