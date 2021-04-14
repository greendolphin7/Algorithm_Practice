# N과 M (2)

N, M = map(int, input().split())

choice = [0] * M
arr = list(i + 1 for i in range(N))
R = M

def comb(idx, start):
    if idx == R:
        print(' '.join(map(str, choice)))
    else:
        for i in range(start, N):
            choice[idx] = arr[i]
            comb(idx + 1, i + 1)
comb(0, 0)