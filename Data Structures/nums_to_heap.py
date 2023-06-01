def nums_to_maxheap(nums):
    i = 0
    while i < len(nums):
        if nums[i] > nums[int((i-1)/2)]:
            tmp = nums[i]
            nums[i] = nums[(i - 1) // 2]
            nums[(i - 1) // 2] = tmp
        i += 1
    return nums


arr = [10, 4, 3, 5, 1]
print(nums_to_maxheap(arr))
