def rotate(A, B):
    for i in range(N):
        for j in range(N):
            B[j][N -1 - i] = A[i][j]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    arr90 = [[0] * N for _ in range(N)]
    arr180 = [[0] * N for _ in range(N)]
    arr270 = [[0] * N for _ in range(N)]

    rotate(arr, arr90)
    rotate(arr90, arr180)
    rotate(arr180, arr270)
    print('#%s' %(tc))
    for i in range(N):
        print(''.join(map(str, arr90[i])), end=' ')
        print(''.join(map(str, arr180[i])), end=' ')
        print(''.join(map(str, arr270[i])), end=' ')
        print()