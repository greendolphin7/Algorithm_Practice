# 소트인사이드

N = input()

data = list()

for i in N:
    data.append(i)

data = sorted(data, reverse=True)

result = ''
for j in data:
    result += j
print(result)



# array = input()

# for i in range(9, -1, -1):
#     for j in array:
#         if int(j) == i:
#             print(i, end='')