# 수 찾기

import sys

def input():
    return sys.stdin.readline()

def binary_search(data, search, start_index, end_index):    # 시작 인덱스와 끝 인덱스를 받아준다.

    while start_index <= end_index:                         # 시작과 끝이 같아질 때 (리스트 갯수가 1개일 때)
        medium = (start_index + end_index) // 2             # 중간 인덱스 구하기

        if search == data[medium]:                          # 리스트 값이 원하는 값과 같다면
            return 1                                        # 1 반환
        elif data[medium] < search:                         # 같이 찾으려는 값보다 작다면
            start_index = medium + 1                        # 시작값을 중간 점 바로 다음으로 정한다.
        else:
            end_index = medium - 1                          # 끝 점을 중간 점 바로 전 인덱스로 정한다.
    return 0


N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
test_list = list(map(int, input().split()))

num_list = sorted(num_list)

for search_num in test_list:
    print(binary_search(num_list, search_num, 0, N - 1))