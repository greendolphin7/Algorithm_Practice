data = [4, 0, 12, 41, 1, 9, 2, 10, 23, 5]

def quick_sort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]

    left = []
    right = []
    for index in range(1, len(data)):
        if data[index] < pivot:
            left.append(data[index])
        else:
            right.append(data[index])

    return quick_sort(left) + [pivot] + quick_sort(right)

sorted_list = quick_sort(data)
print(sorted_list)