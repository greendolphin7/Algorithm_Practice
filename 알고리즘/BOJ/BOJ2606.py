# 바이러스

import sys

def input():
    return sys.stdin.readline()

# DFS 함수 구현
def DFS(v):
    global count
    visited[v] = True
    count += 1
    for e in graph[v]:
        if not visited[e]:
            DFS(e)

N = int(input())
M = int(input())

# 초기 그래프 만들기
graph = [ [] for _ in range(N + 1) ]
# 방문 표시하기 위한 리스트
visited = [False] * (N + 1)

# 그래프 채워넣기
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

# DFS 실행시키기 
# 몇개를 감염시켰는지 갯수 세기위한 전역 변수 count
count = 0
DFS(1)
# 자기 자신 빼고 카운트
print(count - 1)