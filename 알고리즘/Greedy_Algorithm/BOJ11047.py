# 동전 나누기

N, K = input().split(' ')
coins = []
N = int(N)
K = int(K)

for i in range(N):
    coins.extend(input().split())

coins = list(map(int, coins))
coins = reversed(coins)
total_count = 0

for coin in coins:
    if K >= coin:
        coin_count = int(K // coin)
        K -=  coin * coin_count
        total_count += coin_count
        
print(total_count)
