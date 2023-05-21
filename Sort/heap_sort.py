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


def heap_sort(arr):
    n = len(arr)

    # 构建最大堆，从最后一个非叶节点开始进行堆化操作
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # 逐个将堆顶元素（最大值）与当前未排序部分的末尾元素交换，并对剩余元素进行堆化操作
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # 交换堆顶元素与末尾元素
        heapify(arr, i, 0)  # 对剩余元素进行堆化操作

    return arr


# 测试示例
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = heap_sort(arr)
print(sorted_arr)
