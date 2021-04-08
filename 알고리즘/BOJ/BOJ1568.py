# 새

N = int(input())

second = 0
num = 1
while N != 0:
    if N - num < 0:
        num = 1
    N -= num
    num += 1
    second += 1

print(second)