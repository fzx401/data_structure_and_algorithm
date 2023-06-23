def heapify(nums: list, n, root):  # 此时的n不一定是nums的长度，而是给定的nums中我们要让他成堆的范围，也就是说nums[n:]这部分我们不考虑
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < n and nums[left] > nums[largest]:
        largest = left
    if right < n and nums[right] > nums[largest]:
        largest = right

    if largest != root:
        nums[root], nums[largest] = nums[largest], nums[root]
        heapify(nums, n, largest)


def max_heap(nums, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(nums, n, i)


def heap_sort(nums):
    max_heap(nums,len(nums))
    for i in range(len(nums) - 1, 0, -1):
        nums[0], nums[i] = nums[i], nums[0]
        max_heap(nums, i)


arr = [4, 2, 5, 7, 3, 6, 8]
heap_sort(arr)
print(arr)
