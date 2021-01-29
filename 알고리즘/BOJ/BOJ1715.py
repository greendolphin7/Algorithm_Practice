# 카드 정렬하기

import sys
import heapq

def input():
    return (sys.stdin.readline())

N = int(input())

num_list = []  
for i in range(N):
    num_list.extend(input().split())
num_list = list(map(int, num_list))  # 리스트 인트로 바꿔주기

heapq.heapify(num_list)  # 리스트를 힙으로 바꿔주기 O(N)
                         # 힙: 특정한 규칙을 가진 트리로, 최댓값과 최솟값을 빈번하게 찾아야 할 때 쓰인다.
                         # 완전 이진 트리 // 여기서 heapify는 최소 힙으로 정렬
                         # 부모 노드가 자식 노드보다 작다.
                         # 자식끼리는 대소 관계가 성립하지 않고 부모 키 간에만 성립한다.
total_sum = 0
while len(num_list) > 1:
    first_min_num = heapq.heappop(num_list)  # 힙에서 pop으로 최솟값 빼오기
    second_min_num = heapq.heappop(num_list)

    count = first_min_num + second_min_num
    heapq.heappush(num_list, count)  # 힙에 요소 추가하기
    total_sum += count

print(total_sum)