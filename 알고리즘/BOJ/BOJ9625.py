# BABBA

K = int(input())    # 반복 횟수
A = 1               # 초기 A의 갯수
B = 0               # 초기 B의 갯수

for i in range(K):  # K번 반복
    preB = A        # B가 바뀌기 전에 B의 갯수 = A
    A -= A          # A의 갯수는 모두 없어짐
    A += B          # A의 갯수 만큼 B의 갯수가 생김
    B += preB       # 미리 저장해두었던 A의 갯수만큼 B가 생김

print(A, B, end='')