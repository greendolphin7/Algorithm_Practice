# 수 정렬하기 2

import sys

def input():
    return sys.stdin.readline()

n = int(input())

num_list = []
for _ in range(n):
    num_list.append(int(input()))

sorted_list = sorted(num_list)

for num in sorted_list:
    print(num)


'''
# 내장함수를 사용하지 않고 정렬하려고 했으나 메모리 초과가 나오게 되어 이 이상 더 효율적인 
# 정렬 알고리즘을 모르겠다고 판단하였다.
# 아래는 메모리초과가 나온 퀵소트 코드이다.

def quick_sort(data):                   # 퀵소트 구현
    if len(data) <= 1:                  # 데이터가 하나밖에 없다면 바로 반환
        return data
    
    left, right = [], []                # pivot을 기준으로 좌우로 나눔
    pivot = data[0]                     # 현재 pivot은 첫번째 데이터
    
    for index in range(1, len(data)):   # 1 ~ 마지막 인덱스까지 반복해서
        if pivot > data[index]:         # 기준 값 pivot보다 작으면 
            left.append(data[index])    # 왼쪽 리스트에 더하고
            
        else:
            right.append(data[index])   # 기준값보다 크면 오른쪽에 저장
    
    return quick_sort(left) + [pivot] + quick_sort(right)  # 중간에 pivot을 놓고 리스트 합치기 이걸 재귀로 반복
'''