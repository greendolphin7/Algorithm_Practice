# 블랙잭

N, M = map(int, input().split())

card_list = list(map(int, input().split()))

result = 0
for one in range(N):
    for two in range(one + 1, N):
        for three in range(two + 1, N):
            total_sum = card_list[one] + card_list[two] + card_list[three]
            if total_sum > result and total_sum <= M:
                result = total_sum
print(result)