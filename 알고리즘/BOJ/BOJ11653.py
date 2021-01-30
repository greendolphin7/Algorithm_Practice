N = int(input())

for i in range(2, N+1):  # 2 ~ N 까지의 소인수 후보중

    while N % i == 0:  # N이 후보중에서 나누어 떨이지면 -> 소인수 
        print(i)       # 출력하고
        N /= i         # N은 나누어준다.