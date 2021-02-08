# 숫자 카드

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

for i in card_list:
    try:
        print(result[i], end=' ')   # 키 값 있으면 value 출력
    except:
        print(0, end=' ')           # 없으면 0으로 출력
