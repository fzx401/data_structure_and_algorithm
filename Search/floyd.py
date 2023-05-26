def flyod(graph):
    n = len(graph)
    dist = graph
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][ j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

INF = float('inf')
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]
res = flyod(graph)
print(res)