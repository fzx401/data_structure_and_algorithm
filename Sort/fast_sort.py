class FastSort:

    def fast_sort(self, nums):
        if len(nums) % 2 == 0:
            mid_num = nums[int(len(nums)/2)]
        else:
            mid_num = nums[int((len(nums)-1)/2)]
        nums_1 = nums[:nums.index(mid_num)]
        nums_2 = nums[nums.index(mid_num)+1:]
        tmp_1 = []
        tmp_2 = []
        for i in nums_1:
            if i > mid_num:
                nums_1.remove(i)
                tmp_1.append(i)
        for i in nums_2:
            if i < mid_num:
                nums_2.remove(i)
                tmp_2.append(i)
        nums_1 = nums_1 + tmp_2
        nums_2 = nums_2 + tmp_1
        for l in [nums_1,nums_2]:
            if len(l) != 1:
                self.fast_sort(nums_1)
        return nums_1,nums_2

print(FastSort.fast_sort([2, 1, 4, 2, 5]))