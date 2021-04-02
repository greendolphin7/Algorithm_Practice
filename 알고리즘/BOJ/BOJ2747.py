# 피보나치 수

n = int(input())
a = 0
b = 1

i = 0
while i < n:
    a, b = b, a + b
    i += 1

print(a)

### 시간 초과 에러
# N = int(input())

# def pibo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return pibo(n - 1) + pibo(n - 2)

# print(pibo(N))