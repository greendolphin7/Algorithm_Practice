# 원재의 메모리 복구하기

T = int(input())

for tc in range(1, T + 1):
        
    bit = input()
    N = len(bit)
    reset_bit = '0' * N

    bit = list(bit)
    reset_bit = list(reset_bit)

    count = 0
    for i in range(N):
        if bit[i] != reset_bit[i]:
            count += 1
            for j in range(i, N):
                if reset_bit[j] == '1': 
                    reset_bit[j] = '0'

                elif reset_bit[j] == '0':
                    reset_bit[j] = '1'
            
    print('#%s ' %(tc) + str(count))