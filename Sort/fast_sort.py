"""
快速排序算法
"""


class FastSort:

    def fast_sort(self, nums):
        if len(nums) <= 1:
            return nums
        pivot = nums[len(nums) // 2]
        left_pivot = [nums[i] for i in range(len(nums)) if nums[i] < pivot]
        middle = [nums[i] for i in range(len(nums)) if nums[i] == pivot]
        right_pivot = [nums[i] for i in range(len(nums)) if nums[i] > pivot]
        return self.fast_sort(left_pivot) + middle + self.fast_sort(right_pivot)

s = FastSort()
print(s.fast_sort([2, 1, 4, 2, 5]))
