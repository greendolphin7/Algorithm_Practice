# DFS와 BFS

def DFS(graph, start_node):
    visited = []
    need_visit = []
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            if node not in graph:
                return visited
            need_visit.extend(graph[node])
    return visited


def BFS(graph, start_node):
    visited = []
    need_visit = []
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            if node not in graph:
                return visited
            need_visit.extend(graph[node])
    return visited

graph = {}

N, M, start_node = map(int, input().split())

for i in range(M):
    start, end = map(int, input().split())
    if start not in graph.keys():
        graph[start] = []
    if end not in graph.keys():
        graph[end] = []
    graph[start].append(end)
    graph[end].append(start)

for key in graph:
    graph[key].sort(reverse=True)
dfs_visited = DFS(graph, start_node)
for i in dfs_visited:
    print(i, end=' ')

print()

for key in graph:
    graph[key].sort()
bfs_visited = BFS(graph, start_node)
for j in bfs_visited:
    print(j, end=' ') 