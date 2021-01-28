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