total_person_number = int(input())  # 5
time_list = list(map(int, input().split(" ")))  # 3 1 4 3 2

que_time = 0

for i in range(len(time_list)):
    min_time = min(time_list)
    que_time = que_time + que_time + min_time

    a = time_list.index(min_time)
    del time_list[a]

print(que_time)  # 미완성
