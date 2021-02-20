# 슈퍼 마리오

scores = []

for _ in range(10):
    scores.append(int(input()))

def supermario(scores):
    result = []
    total_score = 0
    answer = 0

    for i in scores:
        total_score += i            # 전체 스코어 합을 업데이트
        result.append(total_score)  # 업데이트 한 값을 결과값 리스트에 하나씩 추가해준다

        if total_score == 100:      # 만약 바로 100과 일치하면 그대로 반환
            return 100

        if result[-1] > 100 and len(result) >= 2:  # 100보다 크지만 점수를 2번 먹은 경우
            more_than_100 = abs(100 - result[-1])  # 100에서 뺀 절대값을 기준으로
            less_than_100 = abs(100 - result[-2])

            if more_than_100 == less_than_100:     # 서로의 절대값이 같으면
                answer = result[-1]                # 큰 값을 반환
                return answer
            elif more_than_100 > less_than_100:    # 작은 값이 100에 더 가까우면
                answer = result[-2]                # 작은 값을 반환
                return answer
            else:
                answer = result[-1]                # 반대의 경우 
                return answer                      # 큰 값 반환

        if result[-1] > 100 and len(result) == 1:  # 100보다 크지만 첫번째부터 100을 넘어버린 경우
            answer = result[-1]
            return answer

    answer = result[-1]                            # 마지막으로 최대 결과값을 리턴
    return answer
 
print(supermario(scores))