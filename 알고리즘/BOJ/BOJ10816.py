# 숫자 카드 2
from sys import stdin

n = int(input())
my_card_list = list(map(int, stdin.readline().split()))
m = int(input())
card_list = list(map(int, stdin.readline().split()))

result = {}                         # 딕셔너리로 접근한다.
for i in my_card_list:              # 카드 하나씩 꺼내어 딕셔너리에 저장한다. 
    try:                            # 이때 이미 존재하는 key 값이라면 try문 실행되고 value에 +1 해준다.
        result[i] += 1
    except:                         # 딕셔너리에 없는 key값이라면 except가 실행되며 value는 그냥 1로 저장된다.
        result[i] = 1

print(result)

for i in card_list:
    try:
        print(result[i], end=' ')   # 키 값 있으면 value 출력
    except:
        print(0, end=' ')           # 없으면 0으로 출력



        

### 시간 초과된 시행착오 코드 // 진짜 백준푸는데 시간초과가 너무 많이 나온다. 
### 그만큼 내가 효율적으로 못짜고 있다는 뜻이라고 생각한다.

#################### 시행 착오 1 #######################

# import sys

# n = int(sys.stdin.readline())
# my_card_list = list(map(int, sys.stdin.readline().split()))

# m = int(sys.stdin.readline())
# card_list = list(map(int, sys.stdin.readline().split()))

# result = {}
# for card in card_list:
#     result[card] = 0
# for my_card in my_card_list:
#     if my_card in list(result.keys()):
#         result[my_card] += 1

# for value in result.values():
#     print(value, end=' ')



#################### 시행 착오 2 #######################

# import sys

# n = int(sys.stdin.readline())
# my_card_list = list(map(int, sys.stdin.readline().split()))

# m = int(sys.stdin.readline())
# card_list = list(map(int, sys.stdin.readline().split()))

# result = {}
# for card in card_list:
#     result[card] = 0

# for my_card in my_card_list:

#     if my_card in card_list:
#         result[my_card] += 1

# for value in result.values():
#     print(value, end=' ')