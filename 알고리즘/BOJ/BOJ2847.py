# 게임을 만든 동준이

N = int(input())

levels = []
for i in range(N):
    levels.append(int(input()))

levels.reverse()    # 뒤에서부터 계산하면 그리디로 편하게 풀 수 있기 때문에 리스트를 뒤집는다.
result = 0          # 출력할 값 저장할 변수
for i in range(N - 1):  
    count = 0                                   # 몇개 내려야 하는지 체크하는 변수
    if levels[i] <= levels[i + 1]:              # 큰 레벨이 작은 레벨보다 경험치가 작다면(리스트 거꾸로이기 때문)
        count = levels[i + 1] - levels[i] + 1   # 얼마나 내려야 경험치가 낮아지는지 계산하고
        levels[i + 1] -= count                  # 해당 값은 내려준다. 다음 계산을 위해
        result += count                         # 출력해야 하는 총 값은 업데이트 해준다.
print(result)
