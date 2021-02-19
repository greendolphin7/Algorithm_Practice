# BABBA

K = int(input())
result = 'A'
A_count = result.count('A')
B_count = result.count('B')
while K != 1:
    result = 'A'
    A_count = result.count('A')
    B_count = result.count('B')
    temp_A = ''
    for i in range(A_count):
        temp_A += 'B'
    temp_B = ''
    for j in range(B_count):
        temp_B += 'BA'
    
    result += temp_B + temp_A
    A_count = result.count('A')
    B_count = result.count('B')
    print(result)
    K -= 1

print(A_count, B_count, end='')