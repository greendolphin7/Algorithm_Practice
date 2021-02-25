# 오르막길
N = int(input())

steps = list(map(int, input().split()))

distance = 0
max_step = 0
for i in range(len(steps) - 1):
    if steps[i] >= steps[i + 1]:
        distance = 0
    else:
        distance += steps[i + 1] - steps[i]
    
    if max_step < distance:
        max_step = distance
print(max_step)