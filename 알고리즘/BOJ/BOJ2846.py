# 오르막길

N = int(input())

road = list(map(int, input().split()))

distance = 0
distance_list = []
for i in range(len(road) - 1):
    if road[i + 1] <= road[i]:
        distance = 0
    else:
        distance += road[i + 1] - road[i]
    distance_list.append(distance)
        
print(max(distance_list))