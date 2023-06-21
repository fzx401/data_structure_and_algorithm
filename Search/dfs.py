"""深度优先算法用栈实现（后入先出）"""
"""python中的栈可以通过list实现"""
def dfs_search(graph: dict, start, target):
    visited = set()
    stack = [start]
    
    while stack:
        node = stack.pop()

        if node == target:
            return True
        
        if node not in visited:
            visited.add(node)
            for i in graph[node]:
                stack.append(i)
    return False
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
start='A'
target='D'
print(dfs_search(graph,start,target))
