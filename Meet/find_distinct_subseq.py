def find_subsequences(nums):
    results = []
    backtrack(nums, [], 0, results)
    return results

def backtrack(nums, current, index, results):
    # 将当前结果加入到最终结果中
    if len(current) >= 2:
        results.append(current[:])

    # 回溯的主要逻辑
    used = set()  # 用于记录当前层已经使用过的元素
    for i in range(index, len(nums)):
        if nums[i] in used:
            continue

        # 选择当前元素
        current.append(nums[i])
        used.add(nums[i])

        # 继续探索下一层
        backtrack(nums, current, i + 1, results)

        # 撤销选择
        current.pop()

print(find_subsequences([1, 2, 3, 4]))
