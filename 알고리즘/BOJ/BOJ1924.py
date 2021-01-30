# 2007  // 2007년의 날짜별 요일 맞추기


# 문제 해결 접근 방법: 해당 날짜까지의 날짜의 합을 구한 다음, 7로 나눈 나머지에 따라 요일 배정
month, day = map(int, input().split())

# 각각의 나머지에 맞는 요일 딕셔너리 만들어주기
week_dict = {'0': 'SUN', '1': 'MON', '2': 'TUE', '3': 'WED', '4': 'THU', '5': 'FRI', '6': 'SAT'} 

month_31 = [1, 3, 5, 7, 8, 10, 12]  # 31일 달 
month_30 = [4, 6, 9, 11]  # 30일인 달

total_day = 0  # 전체 날짜 수를 더할 변수
for i in range(1, month):  # 입력받은 전달까지 날짜 더하기
    if i in month_31:      # 31인 달 리스트 안에 있거나
        total_day += 31    
    elif i in month_30:    # 30일인 달 리스트 안에 있으면 계속 더해준다.
        total_day += 30    # 예를 들어, 4월이면, i가 1부터 2, 3월 까지 돌면서 계속 더해준다.
    elif i == 2:
        total_day += 28    # 만약 2월달이 포함되어있다면 28일 더해준다.

total_day += day           # 마지막으로 해당 달의 날짜까지 더하면 날짜의 총합 계산 완료.

week = str(total_day % 7)  # 2007년 1월 1일이 월요일이므로 나머지를 구해서 요일을 배정한다.
answer = week_dict[week]
print(answer)


