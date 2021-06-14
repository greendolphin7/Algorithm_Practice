# 일곱 난쟁이

# data = []
# for i in range(9):
#     height = int(input())
#     data.append(height)

data = list(int(input()) for _ in range(9))


data.sort()
total = sum(data)

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if (total - data[i] - data[j]) == 100:
            for k in range(len(data)):
                if k != i and k != j:
                    print(data[k])
            exit()