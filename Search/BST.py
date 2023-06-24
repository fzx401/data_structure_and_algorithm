"""
二叉搜索树
"""


class BST:

    def _bstify(self, nums, n, root):
        left = 2 * root + 1
        right = 2 * root + 2
        if left >= n:  # 左节点都不存在，右节点一定也不存在
            return
        if right >= n and nums[root] < nums[left]:
            # while nums[tmp] < nums[left]:
            nums[root], nums[left] = nums[left], nums[root]
        if left < n and right < n:
            while not (nums[left] <= nums[root] <= nums[right]):
                if nums[root] < nums[left]:
                    nums[root], nums[left] = nums[left], nums[root]
                if nums[root] > nums[right]:
                    nums[root], nums[right] = nums[right], nums[root]
        self._bstify(nums, n, left)
        self._bstify(nums, n, right)

    def trans_nums_to_bst(self, nums: list):
        for i in range(len(nums) // 2 - 1, -1, -1):
            self._bstify(nums, len(nums), i)


bst = BST()
arr = [1, 2, 3, 4, 5, 6]
bst.trans_nums_to_bst(arr)
print(arr)

# 在arr中查找target是否存在
