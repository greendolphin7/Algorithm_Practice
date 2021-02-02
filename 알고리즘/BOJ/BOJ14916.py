# 거스름돈

coin_list = [5, 2]  
change = int(input())  # 거슬러줄 돈

total_count = 0                     # 거슬러주는 동전 총 갯수
while change >= 0:
    if change % 5 == 0:             # 5원 짜리로 나누어 떨어지면 
        total_count += change // 5  # 동전 갯수 더해주고
        change = 0                  # 거스름돈 0으로 맞춰주고
        break                       # while문 바로 탈출
    else:
        change -= 2                 # 2원 짜리 하나 거슬러주고
        total_count += 1            # 동전 갯수 추가            

if change == 0:
    print(total_count)
else:
    print(-1)                       # 나눌 수 없으면 -1 출력