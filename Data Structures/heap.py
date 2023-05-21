import heapq

def heapify(arr, n, i):
    largest = i  # 初始化最大元素的索引为父节点 i
    left = 2 * i + 1  # 左子节点索引
    right = 2 * i + 2  # 右子节点索引

    # 如果左子节点存在且大于根节点，则更新最大元素的索引
    if left < n and arr[left] > arr[largest]:
        largest = left

    # 如果右子节点存在且大于根节点，则更新最大元素的索引
    if right < n and arr[right] > arr[largest]:
        largest = right

    # 如果最大元素的索引不是父节点 i，则交换父节点与最大元素
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # 对交换后的子树递归进行堆化操作
        heapify(arr, n, largest)
nums = [4, 10, 3, 5, 1]
print(nums)
heapify(nums, 5, 0)
print(nums)

# def create_max_heap(nums: list) -> 'heap':
#     heap = []
#     for num in nums:
#         heapq.heappush(heap, -num)
#     return heap
#
# nums = [4, 10, 3, 5, 1]
# print(nums)
# heapq.heapify(nums)
# print(nums)
# max_heap = create_max_heap(nums)
# # print(max_heap)