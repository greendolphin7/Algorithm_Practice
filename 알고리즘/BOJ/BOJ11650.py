# 좌표 정렬하기

N = int(input())

point_list = []

for p in range(N):
    X, Y = map(int, input().split())
    point_list.append((X, Y))

point_list = sorted(point_list, key=lambda x: (x[0], x[1]))

for i in point_list:
    print(i[0], i[1])