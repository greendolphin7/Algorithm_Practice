# 주유소

import sys

def input():
    return sys.stdin.readline()

N = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))


# 접근 방법: 현재 도착한 도시에서의 기름값이 이전에서 보았던 최소 기름값보다 작으면
# 현재까지 온 거리 * 현재 도시에서의 기름값을 전체 비용에 더해준다.
# 왜냐하면 이번도시에서 최소 기름값은 초기화 될 것이고, 
# 그렇다면 구매했을 기름값은 지금까지 움직였던 거리만큼 이전 도시에서 채우고 왔을 테니까.

total_cost = distances[0] * costs[0]  # 최초 시작 비용은 다음과 같다. 첫번째 도시에서 다음 도시까지
min_cost = costs[0]                   # 최소 기름값은 첫번째 도시로 초기설정
current_distance = 0                  # 현재 얼만큼 움직였는지를 저장하는 변수, 0으로 초기 설정
for index in range(1, len(costs)-1):  # n개의 도시가 있다면 두번째 도시부터 그 전 도시까지 반복
    if costs[index] < min_cost:       # 만약 현재 도시의 기름 값이 지금까지의 최소 기름 값보다 낮았다면
        total_cost += min_cost * current_distance  # 현재까지 이동한 거리에서 과거의 최소 기름값을 더해서 전체비용 업데이트
        current_distance = distances[index]        # 현재 이동한 거리 업데이트
        min_cost = costs[index]                    # 최소 기름 값 업데이트
    else:
        current_distance += distances[index]       # 최소 값이 아니면 다음 도시도 계속 최소 기름 값으로 곱

    if index == len(costs)-2:         # 마지막 도시
        total_cost += min_cost * current_distance

print(total_cost, end='')