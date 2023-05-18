
class Dijkstra:
    def dijstra(self, start, g):
        # 首先罗列出所有涉及到的点
        nodes = list(g.keys())
        diss = {n: float("inf") for n in g.keys()}
        diss[start] = 0  # 构建一个字典，存储从起点到各点的距离，除起点外，各点距离都设为0
        visited = []  # 构建已访问节点的列表，已访问节点实际上就是已确定起点到其最短距离的点

        while len(visited) < len(g):
            #  每轮贪心搜索，从距离起点最近且不在已访问节点的点中找出距离最短的作为探索节点
            current_node = min([node for node in nodes if node not in visited], key=lambda x: diss[x])
            visited.append(current_node)
            for ne in g[current_node].keys():
                dis = diss[current_node] + g[current_node][ne]
                if dis < diss[ne]:
                    diss[ne] = dis
        return diss


# 示例图的邻接表表示
graph = {
    'A': {'B': 5, 'C': 3},
    'B': {'A': 5, 'C': 1, 'D': 2},
    'C': {'A': 3, 'B': 1, 'D': 6},
    'D': {'B': 2, 'C': 6}
}

start_node = 'A'
d = Dijkstra()
distances = d.dijstra(start_node, graph)

# 输出最短距离
for node, distance in distances.items():
    print(f'Shortest distance from {start_node} to {node}: {distance}')

