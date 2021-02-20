# 슈퍼 마리오

scores = []


for _ in range(10):
    scores.append(int(input()))

def supermario(scores):
    result = []
    total_score = 0
    answer = 0

    for i in scores:
        total_score += i
        result.append(total_score)

        if total_score == 100:
            return 100

        if result[-1] > 100 and len(result) >= 2:
            abs1 = abs(100 - result[-1])
            abs2 = abs(100 - result[-2])

            if abs1 == abs2:
                answer = result[-1]
                return answer
            elif abs1 > abs2:
                answer = result[-2]
                return answer
            else:
                answer = result[-1]
                return answer
        if result[-1] > 100 and len(result) == 1:
            answer = result[-1]
            return answer
    answer = result[-1]
    return answer
 
print(supermario(scores))

# # 슈퍼 마리오

# scores = []

# for _ in range(10):
#     scores.append(int(input()))

# def supermario(scores):
#     result = []
#     total_score = 0
#     answer = 0

#     for i in scores:
#         total_score += i
#         result.append(total_score)

#         if total_score == 100:
#             return 100

#         if total_score < 100:
#             continue
#         else:                   # 100 보다 크면 비교해야 함
#             more_than_100 = abs(100 - max(result))
#             less_than_100 = abs(100 - result[-2])

#             if 
#     answer = result[-1]

#     return answer
 
# print(supermario(scores))