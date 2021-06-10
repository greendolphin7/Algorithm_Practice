# 분해합

N = int(input())

for i in range(1, N):
    sum_num = i

    str_i = str(i)
    for j in str_i:
        sum_num += int(j)

    if sum_num == N:
        print(i)
        break
else:
    print(0)
