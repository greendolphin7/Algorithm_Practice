# 단어 공부

import sys

def input():
    return sys.stdin.readline().strip()

word = input()
word = word.lower()   # 대소문자 구분이 없으니 단어를 모두 소문자로 변경
count_dict = {}       # 각 단어들이 몇개 나왔는지 카운트하기 위해 딕셔너리 생성
for i in range(len(word)):
    if word[i] in count_dict.keys():
        count_dict[word[i]] += 1   # 이미 나온 문자라면 카운트 추가
    else:
        count_dict[word[i]] = 1    # 새로 나온 문자라면 1로 초기화 


# 값을 기준으로 내림차순 정렬하기 위한 함수
def sort_dictionary(dic): 
    return sorted(dic.items(), key=lambda x: x[1], reverse=True)    


items = sort_dictionary(count_dict)

if len(items) >= 2:
    if items[0][1] == items[1][1]:  # 카운트가 동일하다면 ? 출력
        print('?')
    else:
        print(items[0][0].upper())
else:
    print(items[0][0].upper())