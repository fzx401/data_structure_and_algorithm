class Solution:
    def permute(self, nums):
        res = []

        def backtrack(nums, tmp):  # nums代表剩余选择，tmp代表已做出的决策
            if not nums:  # 如果此时已经没有剩余选项，则进行回溯，return则会返回回溯树上一层
                res.append(tmp)
                return
            for i in range(len(nums)):  # 从当前可选的选项（分支）中依次寻找
                backtrack(nums[:i] + nums[i + 1:], tmp + [nums[i]])

        backtrack(nums, [])
        return res


# 示例用法
s = Solution()
nums = [1, 2, 3]
subsequences = s.permute(nums)
print(subsequences)
