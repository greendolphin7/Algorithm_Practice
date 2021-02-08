# 음계

a = list(map(int, input().split(' ')))
score = 0

for i in range(len(a) - 1):  # 전체 음계 반복
    if a[i] - a[i+1] == -1:  # 만약 낮아지는 음계라면 descending
        score = score + 1
    elif a[i] - a[i+1] == 1: # 높아지는 음계라면 ascending
        score = score - 1
    else:
        score = score + 0    # 아무것도 아니면 mixed
        
if score == len(a) - 1:      # 전체 스코어가 계속 올라갔다면
    print('ascending')
elif score == (len(a) * -1) + 1:  # 전체 스코어가 계속 내려갔다면
    print('descending')
else:
    print('mixed')           # 그 외