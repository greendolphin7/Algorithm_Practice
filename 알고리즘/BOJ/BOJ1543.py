# 문서 검색

doc = input()
word = input()

count = 0
i = 0
while i < len(doc):
    if word == doc[i:i+len(word)]:
        count += 1
        i += len(word)
    else:
        i += 1
print(count)