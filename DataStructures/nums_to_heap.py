def nums_to_maxheap(nums):
    for i in range(len(nums)):
        while nums[i] > nums[int((i-1/2))]:
            tmp = nums[i]
            nums[i] = nums[int((i-1)/2)]
            nums[int((i-1)/2)] = tmp
            i = int((i-1)/2)
    return nums


arr = [1, 4, 3, 5, 10]
print(nums_to_maxheap(arr))
