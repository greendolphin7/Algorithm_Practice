# 수 찾기

N = int(input())
check_list = list(map(int, input().split()))

M = int(input())
answer_num = list(map(int, input().split()))

def binary_search(s, e, data, num):
    while s <= e:
        mid = (s + e) // 2
        if data[mid] == num:
            return 1

        elif data[mid] < num:
            s = mid + 1
        else:
            e = mid - 1
    return 0

check_list.sort()
for i in answer_num:
    result = binary_search(0, N - 1, check_list, i)
    print(result)