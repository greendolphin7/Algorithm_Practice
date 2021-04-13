# 트로피 진열

N = int(input())

trop = []
for i in range(N):
    trop.append(int(input()))

def ascending(trop):
    now = trop[0]
    count = 1
    for i in range(1, len(trop)):
        if trop[i] > now:
            count += 1
            now = trop[i]
    return count

left_count = ascending(trop)
trop.reverse()
right_count = ascending(trop)

print(left_count)
print(right_count)