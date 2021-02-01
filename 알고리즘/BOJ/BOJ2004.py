# 조합 0의 개수

import math
import sys

def input():
    return (sys.stdin.readline())

n, m = map(int, input().split())

# 접근 방법: 뒷자리수가 0이라는 건 10을 곱했다는 의미이다. 
# 10을 곱하기 위해선 2와 5가 곱해진 것.
# 따라서 조합에서 2와 5가 몇번 짝지어 곱해진 것인지 구하면 된다.
# 이항계수 성질에 의해 nCm = n! / (m! * (n - m)!)
# 따라서 n!에서의 2와 5의 갯수에서 m!, (n-m)!의 갯수를 빼주면 된다.


# 5의 갯수 세기
def count_five(n):
    count = 0
    while n != 0:
        n = n // 5  # 팩토리얼 곱에서 n // 5의 몫 만큼 5의 갯수가 있다.
        count += n
    return count

# 2의 갯수 세기
def count_two(n):
    count = 0
    while n != 0:
        n = n // 2  # 팩토리얼 곱에서 n // 2의 몫 만큼 2의 갯수가 있다.
        count += n
    return count

total_two =  count_two(n) - count_two(m) - count_two(n-m)
total_five = count_five(n) - count_five(m) - count_five(n-m)

answer = min(total_two, total_five)
print(answer)


### 시행착오 - 직접 팩토리얼 계산을 통해 답을 구하려고 하면 시간초과가 나오게 된다.

# 아래는 직접 팩토리얼을 구해서 답을 구하려고 했던 시행착오 코드이다.

# combination = int(math.factorial(n) / (math.factorial(m) * math.factorial(n-m)))
# combination = str(combination)[::-1]
# combination = combination[::-1]