# 나이순 정렬

N = int(input())

p_list = []

for _ in range(N):
    age, name = input().split()
    age = int(age)
    person = (age, name)

    p_list.append(person)

p_list = sorted(p_list, key=lambda x: x[0])

for person in p_list:
    print(person[0], person[1])
