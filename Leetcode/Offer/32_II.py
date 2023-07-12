from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val):
        self.root = val
        self.left = None
        self.right = None


class Solution:

    def levelOrder(self, root: TreeNode) -> None | List[List[int]]:
        if not root:
            return []
        res, queue = [], deque()
        queue.append(root)
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmp)
        return res
