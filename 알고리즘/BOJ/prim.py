from collections import defaultdict
from heapq import *

myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]


def prim(start_node, edges):
    # 최소 신장트리를 넣어줄 리스트
    mst = list()
    # 노드의 인접한 간선들을 저장할 딕셔너리
    adjacent_edges = defaultdict(list)
    # 간선들 정보에서 가중치, 노드 두개를 인접 리스트에 딕셔너리 형태로 추가
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    # 연결된 노드 정보들 저장할 곳에 중복없이 저장, 맨 처음 값은 시작 정점으로 초기화
    connected_nodes = set(start_node)
    # 최소 신장 트리에 넣을 후보군들을 저장할 리스트, 시작 정점으로 초기화
    candidate_edge_list = adjacent_edges[start_node]
    # 최소 힙으로 만들어줌. -> 가중치 가장 낮은 것부터 빼내기 위함
    heapify(candidate_edge_list)

    # 후보군이 없어질 때까지 계속 반복
    while candidate_edge_list:
        # 노드 하나 빼면 얻을 수 있는 정보
        weight, n1, n2 = heappop(candidate_edge_list)
        # 만약에 상대 정점이 현재 연결된 노드들 리스트에 없으면
        if n2 not in connected_nodes:
            # 해당 노드를 추가시켜주고 (사이클이 생기는 경우를 없애기 위해)
            connected_nodes.add(n2)
            # 최소 신장트리에도 넣어준다.
            mst.append((weight, n1, n2))

            # 반복적으로 해당 노드에 연결된 다른 노드들도 후보리스트에 넣어주기
            for edge in adjacent_edges[n2]:
                # 상대 노드가 연결 노드에 없으면 넣어주기
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)

    return mst


print(prim('A', myedges))