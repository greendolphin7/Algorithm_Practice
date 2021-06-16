# 요세푸스 문제
from collections import deque
N, K = map(int, input().split())

people = list()
people = deque(i for i in range(1, N + 1))
answer = []
while len(people) != 0:
    for i in range(K - 1):
        move_person = people.popleft()
        people.append(move_person)
    answer.append(str(people.popleft()))

result = ', '.join(answer)
print('<' + result + '>')
