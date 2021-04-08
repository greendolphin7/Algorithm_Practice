# 베스트셀러

N = int(input())

best_seller = {}

for _ in range(N):
    book = input()
    if book in best_seller.keys():
        best_seller[book] += 1
    else:
        best_seller[book] = 1

target = max(best_seller.values())
arr = []
for title, number in best_seller.items():
    if number == target:
        arr.append(title)

arr.sort()
print(arr[0])