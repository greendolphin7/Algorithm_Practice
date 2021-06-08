# 더하기 싸이클

N = int(input())

def make_new_num(num):
    num1 = num // 10  # 십의 자리
    num2 = num % 10   # 일의 자리
    num3 = (num1 + num2) % 10
    new_number = num2 * 10 + num3

    return new_number

count = 0
new_number = N
num = N
while True:
    new_number = make_new_num(num)
    num = new_number
    count += 1
    if N == new_number:
        break

if count == 0:
    count += 1

print(count)
