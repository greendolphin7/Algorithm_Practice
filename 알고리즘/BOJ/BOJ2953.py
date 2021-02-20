# 나는 요리사다
score_list = []

for i in range(5):
    score = list(map(int, input().split()))
    score_list.append(score)

first_prize = 0  # 1등한 요리사
first_score = 0  # 1등 요리사의 점수

for cook in range(len(score_list)):
    cook_score = 0                          # 요리사 점수를 하나씩 더하기 위한 변수
    for j in range(len(score_list[cook])):  # 요리사 한명의 점수리스트를 반복
        cook_score += score_list[cook][j]

    if cook_score > first_score:            # 지금까지 점수가 가장 큰 사람이 있다면
        first_score = cook_score            # 교환
        first_prize = cook                  # 1등 요리사도 업데이트

first_prize += 1                 # 인덱스는 0부터 시작하고 요리사는 1번 요리사부터 시작하니까 1 더해주기
print(first_prize, first_score)  # 출력