# 크로아티아 알파벳

word_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

string = input()

for word in word_list:
    string = string.replace(word, '*')

result = len(string)
print(result)