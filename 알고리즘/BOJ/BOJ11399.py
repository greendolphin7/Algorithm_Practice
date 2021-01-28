# ATM

total_person_number = int(input())  # 5
time_list = list(map(int, input().split(" ")))  # 3 1 4 3 2

que_time = 0
que_list = []
time_list = sorted(time_list)  # 먼저 시간 정렬

for i in time_list:  # 정렬된 시간에서
    que_time += i  # 대기시간 계산
    que_list.append(que_time)  # 계산된 대기시간 리스트에 저장

print(sum(que_list))  # 대기시간 리스트 총합 계산해서 출력
