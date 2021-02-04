# 수 정렬하기 3

import sys

def input():
    return sys.stdin.readline()

n = int(input())

# 접근 방법: 숫자들을 리스트에 저장해두고 리스트끼리 계산해서 풀면 안된다. (메모리 초과)

# 10000개의 요소가 들어갈 수 있는 리스트를 만들고 난 후 (각각의 요소들은 모두 0)
# 들어오는 숫자들을 리스트의 해당 인덱스에 1씩 추가해준다.
# 리스트를 앞에서부터 순서에 맞게 출력해준다.


num_list = [0 for i in range(10000)]            # 요소가 모드 0인 길이 10000 리스트 생성

for num in range(n):                            # 전체 갯수 만큼 반복하면서
    num_list[int(input())-1] += 1               # 1~10000의 자연수이기 때문에 해당 인덱스가 곧 숫자 -> 나오면 해당 인덱스에 1추가 (중복 포함)

for index in range(len(num_list)):              # 인덱스에 갯수 저장되어 있는 리스트 반복
    if num_list[index] != 0:                    # 인덱스가 0이 아니면 -> 숫자 입력 받았으면
        for repeat in range(num_list[index]):   # 그 숫자(해당 숫자 입력 받은 수)만큼 출력
            print(index+1)                      # 인덱스 + 1 이 진짜 숫자 (인덱스는 0부터 시작)
