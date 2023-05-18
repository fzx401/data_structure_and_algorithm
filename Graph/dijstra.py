import numpy as np
import pandas as pd
class Dijstra:
    def dijstra(self, start, graph):
        nodes = list(graph.keys())
        distances = {node: float("inf") for node in graph.keys()}
        distances[start] = 0
        visited = []

        while len(visited) < len(graph):
            current_node = min([node for node in nodes if node not in visited], key=lambda x: distances[x])
            visited.append(current_node)
            for ne in graph[current_node].keys():
                distance = distances[current_node] + graph[current_node][ne]
                if distance < distances[ne]:
                    distances[ne] = distance
        return distances


# 示例图的邻接表表示
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 1, 'D': 2},
    'C': {'A': 3, 'B': 1, 'D': 6},
    'D': {'B': 2, 'C': 6}
}

start_node = 'A'
d = Dijstra()
distances = d.dijstra(start_node, graph)

# 输出最短距离
for node, distance in distances.items():
    print(f'Shortest distance from {start_node} to {node}: {distance}')

