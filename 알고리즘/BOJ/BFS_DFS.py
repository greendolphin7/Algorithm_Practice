def DFS(graph, start_node):
    visited = []
    need_visited = []
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited


def BFS(graph, start_node):
    visited = []
    need_visited = []
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.pop(0)
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

    
graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

visited_dfs = DFS(graph, 'A')
print(visited_dfs)
visited_bfs = BFS(graph, 'A')
print(visited_bfs)