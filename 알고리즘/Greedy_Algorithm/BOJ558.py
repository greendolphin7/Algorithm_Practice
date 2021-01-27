N = int(input())  # 1 ~ 999 사이 정수

N = 1000 - N  # 1000원을 내었을 때 거스름돈 총합

coin_list = [500, 100, 50, 10, 5 , 1] # 동전 리스트

total_count = 0  # 출력할 카운트
for coin in coin_list:  # 동전 리스트 큰 단위부터 하나하나씩 반복
    if N >= coin:  # 거스름돈 총합보다 동전 단위가 더 크면
        count = N // coin  # 몇개 낼 수 있는지 카운트해서
        total_count += count  # 총 카운트 갯수에 업데이트
        N -= count * coin  # 거스름돈 낸 금액 업데이트

print(total_count)  # 출력