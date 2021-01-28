# 단어 수학

import sys

def input():
    return (sys.stdin.readline())

N = int(input())

word_list = []
for i in range(N):
    word_list.extend(input().split())


def cal_num(word_list):
    num = [n for n in range(10)]  # 0 ~ 9 까지의 숫자 미리 만들어두기

    word_dict = {}  # {알파벳: 알파벳 더해지는 값의 합} 

    for word in word_list:  # 단어 하나씩 반복
        for char in range(len(word)):  # 단어 하나에서 알파벳 하나씩 반복
            if word[char] not in word_dict.keys():  # 만약 키 리스트에 없다면
                word_dict[word[char]] = 10 ** (len(word)-char-1)  # 키 추가하고 자리수에 따라 계산되는 값 계산
            else:  # 키 리스트에 있다면 값 업데이트
                word_dict[word[char]] = word_dict[word[char]] + 10 ** (len(word)-char-1)

    values = sorted(list(word_dict.values()), reverse=True)  # 계산 값을 내림차순으로 정렬

    key_list = list(word_dict.keys())  # 키를 정렬 시킨 후 -> (계산값 * 숫자) 하기 위해 키 정렬

    for i in range(len(key_list)-1):  # 키 버블 정렬
        for j in range(len(key_list)-i-1):
            if word_dict[key_list[j]] < word_dict[key_list[j+1]]:  
                key_list[j], key_list[j+1] = key_list[j+1], key_list[j]

    total_sum = 0
    for key in key_list:
        total_sum += num.pop() * word_dict[key]  # 0 ~ 9 에서 하나씩 꺼내서 곱해서 더하기 // 0 ~ 9 숫자 * 그 숫자가 총 계산되는 값
    
    return total_sum

print(cal_num(word_list))


### 시행착오 코드  // 가장 긴 단어 첫머리를 찾는 것보다 가중치 계산 후 키를 이용한 접근이 더 수월하다.

### 아래 코드는 ABC, CBA, CCC 경우일 때 최적값을 못찾는다.

# import sys
# import copy

# def input():
#     return (sys.stdin.readline())

# N = int(input())

# word_list = []
# for i in range(N):
#     word_list.extend(input().split())


# def return_word_length(word_list):
#     word_length_list = []

#     for word in word_list:
#         word_length = len(word)
#         word_length_list.append(word_length)
#     return word_length_list


# def return_word_dict(word_list):
#     word_dict = {}
#     int_list = [n for n in range(9, -1, -1)]
#     word_length_list = return_word_length(word_list)

#     while max(word_length_list) > 0:
#         word_length_list = return_word_length(word_list)  # 단어 길이 저장한 리스트

#         longest_word_index = word_length_list.index(max(word_length_list))  # 그중에서 가장 큰 값 찾기
        
#         longest_word = word_list[longest_word_index]  # 인덱스로 단어 찾기

#         if len(longest_word) > 0:       # 단어 자릿수 체크
#             alphabet = longest_word[0]  # 단어 맨 앞자리 찾기
#         else:                           # 단어 부족하면
#             continue                    # 다시 돌리기

#         if alphabet in word_dict.keys():  # 해당 알파벳이 키에 이미 있으면 
#             longest_word = longest_word[1:]  # 없애고 
#             word_list[longest_word_index] = longest_word
#             continue                        # 다시 돌리기

#         word_dict[alphabet] = int_list[0]  # 딕셔너리에 키값과 밸류값 정해주기
#         int_list = int_list[1:]         # 쓴 밸류 숫자 없애주기
#         longest_word = longest_word[1:]  # 현재 가장 큰 단어 줄이기

#         word_list[longest_word_index] = longest_word  # 단어 리스트 업데이트

#     return word_dict


# def word_to_int(word_list):
#     temp = copy.deepcopy(word_list)
#     total_sum = 0
#     word_to_int_list = []
#     word_dict = return_word_dict(word_list)
#     print(word_dict)

#     for word in temp:
#         char_sum = ''
#         for char in word:
#             int_to = word_dict[char]
#             char_sum += str(int_to)

#         word_to_int_list.append(char_sum)
#     word_to_int_list = map(int, word_to_int_list)

#     return sum(word_to_int_list)
        
# print(word_to_int(word_list))