from collections import deque


def all_city():
    inputs = [
        [1, 2],
        [1, 3],
        [2, 3],
        [2, 4]
    ]
    graph_size = 4
    start = 1
    graph = [[] for _ in range(graph_size + 1)]
    for s, e in inputs:
        graph[s].append(e)

    queue = deque([start])
    distance = [-1] * (graph_size + 1)
    distance[start] = 0
    while queue:
        node = queue.popleft()
        for sub_node in graph[node]:
            if distance[sub_node] == -1:
                queue.append(sub_node)
                distance[sub_node] = distance[node] + 1
    print(distance)


all_city()
