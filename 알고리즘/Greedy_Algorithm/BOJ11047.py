# 동전 나누기

N, K = input().split(' ')  # 입력 받기
coins = []  # 동전 종류 넣을 리스트
N = int(N)
K = int(K)

for i in range(N):  
    coins.extend(input().split())  # 동전들 리스트에 넣어주기

coins = list(map(int, coins))  # 동전들 인트로 바꾸기
coins = reversed(coins)  # 내림차순으로 정렬
total_count = 0  # 전체 동전 갯수

for coin in coins:  # 동전 리스트 반복
    if K >= coin:  # 만약 바꿔줄 돈이 동전 표시금액보다 작으면 -> 바꿔 줄 수 있다.
        coin_count = int(K // coin)  # 몫만 카운트
        K -=  coin * coin_count  # 줄 돈은 업데이트
        total_count += coin_count  # 전체 동전 갯수에 업데이트
        
print(total_count)  # 출력
