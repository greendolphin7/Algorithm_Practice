# 로프

N = int(input())
ropes = []
for i in range(N):
    ropes.append(int(input()))  # 밧줄 리스트 넣어주기

ropes_list = sorted(ropes)  # 오름 차순으로 정렬

total_strength = 0  # 업데이트 해줄 최대 힘

for i in range(len(ropes_list)):  
    strength = ropes_list[i] * (len(ropes_list) - i)  # 첫번째가 가장 작은 힘 * 갯수

    if total_strength < strength:  # 최대 힘이 더 커지면 
         total_strength = strength  # 업데이트

print(total_strength)


## 아래 코드들은 시행착오들 (시간 초과)

# total_strength = 0
# for rope in ropes:
#     min_strength = min(ropes)

#     strength = min_strength * len(ropes)

#     if total_strength < strength:
#         total_strength = strength

#     ropes.remove(rope)

# print(total_strength)


# total_strength = 0
# for rope in ropes:
#     weakest_rope = rope  # 가장 약한 밧줄이라고 가정

#     num = 0
#     for stronger in ropes:
#         if weakest_rope <= stronger:
#             num += 1

#     strength = weakest_rope * num

#     if total_strength < strength:
#         total_strength = strength

# print(total_strength)
