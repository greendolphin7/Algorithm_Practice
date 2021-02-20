# 크로스워드 만들기

word1, word2 = input().split()
plate = [['.'] * len(word1) for _ in range(len(word2))]  # [['.'], ['.'], ['.']] 형식으로 리스트 생성


# 두 단어 중에 같은 단어 찾는 함수
def find_same_word(word1, word2):
    for i in word1:
        for j in word2:
            if i == j:
                return i
    return '같은 문자 없음'

# 한 단어에서 특정 문자의 인덱스 찾는 함수
def find_same_word_index(word, search_word):
    index = 0
    for i in range(len(word)):
        if word[i] == search_word:
            return i
    return '없어'


same_word = find_same_word(word1, word2)    # 같은 단어 변수 저장
same_word_index_word1 = find_same_word_index(word1, same_word)  # 인덱스 저장
same_word_index_word2 = find_same_word_index(word2, same_word)  # 인덱스 저장


for i in range(len(plate)):         # 전체 배열안에 요소 갯수: 행의 갯수

    if i == same_word_index_word2:  # 만약 가로로 넣어야하는 행이 i와 일치하면
        for j in range(len(word1)): # 단어 하나하나를 행과 열에 맞게 넣어준다.
            plate[same_word_index_word2][j] = word1[j]  # 배열[행][열]에 단어 하나씩 넣기

    for k in range(len(plate)):                     # i 돌면서 매 행에서 특정 열 부분만 
        plate[k][same_word_index_word1] = word2[k]  # 모든 행에 대해서 일치하는 특정 열만 단어 넣기

for row in range(len(plate)):
    print(''.join(plate[row]))   # join으로 출력
