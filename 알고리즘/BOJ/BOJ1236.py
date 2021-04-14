# 성 지키기

N, M = map(int, input().split())
castle = [list(input()) for i in range(N)]

r_count = [0] * N
c_count = [0] * M


for r in range(N):
    for c in range(M):
        if castle[r][c] == 'X':
            r_count[r] = 1
            c_count[c] = 1

row = 0
column = 0
for r in range(N):
    if r_count[r] == 0:
        row += 1

for c in range(M):
    if c_count[c] == 0:
        column += 1

print(max(row, column))