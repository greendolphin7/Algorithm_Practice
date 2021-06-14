# 일곱 난쟁이

data = []
for i in range(9):
    height = int(input())
    data.append(height)

data.sort()
total = sum(data)

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if (total - data[i] - data[j]) == 100:
            for a in data:
                if a != data[i] and a != data[j]:
                    print(a)
            exit()