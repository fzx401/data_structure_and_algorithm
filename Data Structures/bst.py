class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find(self, data):
        if data < self.data:
            if self.left is None:
                return None
            return self.left.find(data)
        elif data > self.data:
            if self.right is None:
                return None
            return self.right.find(data)
        else:
            return self

    def delete(self, data):
        if self is None:
            return self

        if data < self.data:
            #  每次删除实际上都是一次搜索
            #  从根节点开始比较大小
            self.left = self.left.delete(data)
        elif data > self.data:
            self.right = self.right.delete(data)
        else:
            if self.left is None:
                temp = self.right
                self = None
                return temp
            elif self.right is None:
                temp = self.left
                self = None
                return temp
            temp = self.right.minimum()
            self.data = temp.data
            self.right = self.right.delete(temp.data)
        return self

    def minimum(self):
        #  直到找到没有左子树的节点为止，直接返回
        if self.left is None:
            return self
        return self.left.minimum()

    def is_bst(self):
        if self.left:
            if self.left.data > self.data or not self.left.is_bst():
                return False

        if self.right:
            if self.right.data < self.data or not self.right.is_bst():
                return False

        return True

    def height(self, node):
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return max(left_height, right_height) + 1

    def inorder_traversal(self, root):
        res = []
        if root:
            #  先对左子树递归遍历
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            #  再对右子树递归遍历
            res = res + self.inorder_traversal(root.right)
        return res

if __name__ == '__main__':
    # 创建二叉树
    root = Node(50)
    root.insert(30)
    root.insert(20)
    root.insert(40)
    root.insert(70)
    root.insert(60)
    root.insert(80)

    # 删除节点
    print("Deleting node 20:")
    root.delete(20)
    print(root.inorder_traversal(root))

    # 判断是否为二叉搜索树
    print("Is it a BST?:", root.is_bst())

    # 计算树的深度
    print("Tree height:", root.height(root))
