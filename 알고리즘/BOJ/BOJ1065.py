# 한수

N = int(input())
count = 0
if len(str(N)) <= 2:
    print(N)
else:
    for n in range(N, 100, -1):
        num = str(n)
        first_difference = int(num[0]) - int(num[1])
        flag = False
        for i in range(len(str(n)) - 1):
            
            next_difference = int(num[i]) - int(num[i + 1])
            if first_difference != next_difference:
                flag = False
                break
            else:
                flag = True
        if flag == True:
            count += 1

    print(count + 99)
