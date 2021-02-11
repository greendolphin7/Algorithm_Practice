# 카드

import sys

def input():
    return sys.stdin.readline()

N = int(input())

num_dict = {}                       # key: value 를 카드: 갯수 형태로 만들어주기 위한 딕셔너리 생성
for i in range(N):                  # 전체 카드 갯수 만큼 반복
    number = int(input())

    if number in num_dict.keys():   # 만약에 딕셔너리 안에 있는 중복 카드라면
        num_dict[number] += 1       # 갯수 1씩 더해주기

    else:                           # 새로운 카드라면
        num_dict[number] = 1        # 1로 초기화

biggest_value = 0                   # 카드 몇개 있는지 나타내는 변수
result = 0                          # 해당 카드 (key)
for item in num_dict.items():       # item 만큼 반복하면서
    if item[1] > biggest_value:     # 현재 가장 큰 갯수를 가지고 있는 카드가 바뀌면 
        biggest_value = item[1]     # 값 업데이트 해주고
        result = item[0]            # 해당 카드 저장
    elif item[1] == biggest_value:  # 그런데 만약 갯수가 같다면
        if result < item[0]:        # 더 작은 카드가 아니라면 넘기고
            continue
        else:                       # 더 작은 카드면 바꿔준다.
            result = item[0]
        
print(result)