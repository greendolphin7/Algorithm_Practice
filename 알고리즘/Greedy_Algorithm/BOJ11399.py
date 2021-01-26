# ATM

total_person_number = int(input())  # 5
time_list = list(map(int, input().split(" ")))  # 3 1 4 3 2

que_time = 0
que_list = []
time_list = sorted(time_list)

for i in time_list:
    que_time += i
    que_list.append(que_time)

print(sum(que_list))