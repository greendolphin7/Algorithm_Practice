# 분할정복 병합정렬

def mergesplit(data):
    if len(data) <= 1:
        return data
    medium = int(len(data) / 2)
    left = mergesplit(data[:medium])
    right = mergesplit(data[medium:])
    
    return merge(left, right)


def merge(left, right):
    global check

    left_point, right_point = 0, 0
    
    merged_list = []
    if left[-1] > right[-1]:
        check += 1
    
    # 아직 둘다 남아 있는 경우
    while len(left) > left_point and len(right) > right_point:
        if left[left_point] > right[right_point]:
            merged_list.append(right[right_point])
            right_point += 1
        else:
            merged_list.append(left[left_point])
            left_point += 1
    
    # 왼쪽이 없는 경우
    while len(left) > left_point:
        merged_list.append(left[left_point])
        left_point += 1
    
    # 오른쪽이 없는 경우
    while len(right) > right_point:
        merged_list.append(right[right_point])
        right_point += 1
        
    return merged_list

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    sample_list = list(map(int, input().split()))
    check = 0
    result_list = mergesplit(sample_list)
    result = result_list[N // 2]

    print('#%d' %(tc), result, check) 
