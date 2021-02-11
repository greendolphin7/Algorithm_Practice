# 암기왕

import sys

def input():
    return sys.stdin.readline()

T = int(input())

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

for test_case in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))
    M = int(input())
    test_list = list(map(int, input().split()))

    num_list = sorted(num_list)
    
    for search_num in test_list:
        print(binary_search(num_list, search_num, 0, N - 1))

########################## 시행 착오 코드 ###############################

# 이진 탐색 문제를 해결하는 코드를 작성하였지만 자꾸 시간초과 문제가 나오게 되어 부득이하게
# 검색을 하게 되었다. 검색을 통해 통과한 코드가 위의 코드이며
# 아래는 시행착오를 거친 코드이다. 답은 정확하게 출력하지만 시간초과가 나오게 된다.
# 재귀를 활용하였다.

# import sys

# def input():
#     return sys.stdin.readline()

# T = int(input())



# def binary_search(data, search):
#     data = sorted(data)
#     data_len = len(data)
#     if search == data[0] and data_len == 1:
#         return True

#     if search != data[0] and data_len == 1:
#         return False
    
#     medium = data_len // 2
#     if search == data[medium]:
#         return True
#     else:
#         if data[medium] > search:
#             return binary_search(data[:medium], search)
#         else:
#             return binary_search(data[medium:], search)


# for test_case in range(T):
#     N = int(input())
#     num_list = list(map(int, input().split()))
#     M = int(input())
#     test_list = list(map(int, input().split()))
    
#     for i in range(M):
#         search_num = test_list[i]

#         if binary_search(num_list, search_num) == True:
#             print(1)
#         else:
#             print(0)