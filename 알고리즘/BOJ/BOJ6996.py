# 애너그램

import sys

n = int(sys.stdin.readline())

word_list = []
for i in range(n):
    word_ = list(sys.stdin.readline().split())
    word_list.append(word_)

for word_pair in word_list:     # 두 단어를 리스트 안에 리스트로 저장하였다. // [['단어', '단어'], ['단어', '단어']]
    
    # 문자 갯수가 다르면 바로 서로 애너그램이 아니라고 출력
    if len(word_pair[0]) != len(word_pair[1]):
        print(f'{word_pair[0]} & {word_pair[1]} are NOT anagrams.')
    else:
        # 딕셔너리 객체를 넣어줄 리스트 생성
        word_dict_list = []
        # 단어 두개 있는 리스트 안에 단어 하나를 반복
        for word in word_pair:
            word_dict = {}  # 딕셔너리는 문자: 단어 안에 있는 문자 갯수 형태로 지정하기 위해 생성
            # 단어 하나하나의 문자들을 반복
            for char in word:
                # 이미 키 값에 있으면 
                if char in word_dict.keys():
                    # value 값에 추가
                    word_dict[char] += 1
                # 없으면
                else:
                    # 키 값 새로 생성하고 1로 지정
                    word_dict[char] = 1  
            word_dict_list.append(word_dict)

        if word_dict_list[0].items() == word_dict_list[1].items():
            print(f'{word_pair[0]} & {word_pair[1]} are anagrams.')
        else:
            print(f'{word_pair[0]} & {word_pair[1]} are NOT anagrams.')
