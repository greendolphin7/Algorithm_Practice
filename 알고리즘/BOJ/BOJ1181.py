# 단어 정렬

import sys

def input():
    return sys.stdin.readline().strip()

N = int(input())

word_list = []
for i in range(N):
    word = input()
    word_list.append(word)

# 접근 방법 : 중복제거는 set을 이용해주고, 순서는 튜플을 이용하면 편하다
word_list = set(word_list)
word_list = list(word_list)

sorted_word_list = []
for word in word_list:
    sorted_word_list.append((len(word), word))  # 핵심! 단어 길이와 해당 단어를 튜플 형식으로 저장한다.

sorted_word_list = sorted(sorted_word_list)   # 튜플로 저장했기 때문에 바로 정렬이 가능하다.

for len_word, word in sorted_word_list:
    print(word)





# 시간초과 오류
# N = int(input())
# answer = []
# for i in range(N):
#     word = input()
#     answer.append(word)

# def sort_word(data):                
#     data = set(data)                # 중복 제거하기 위해 set 사용
#     data = list(data)
#     result = []
#     for i in range(len(data)):      # 버블정렬 형식으로 정렬
#         for j in range(len(data)):
#             if len(data[i]) < len(data[j]):
#                 data[i], data[j] = data[j], data[i]

#             elif len(data[i]) == len(data[j]):  # 만약 두 단어의 길이가 같으면 
#                 if data[i] < data[j]:           # 알파벳 순서를 비교
#                     data[i], data[j] = data[j], data[i]   # 바꿀 단어가 더 작으면 바꿔준다
#     return data

# answer = sort_word(answer)
# for i in range(len(answer)):
#     print(answer[i])