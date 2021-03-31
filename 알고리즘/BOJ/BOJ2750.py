# 수 정렬하기

N = int(input())

num_list = []
for i in range(N):
    num_list.append(int(input()))

num_list = sorted(num_list)

for j in num_list:
    print(j)
