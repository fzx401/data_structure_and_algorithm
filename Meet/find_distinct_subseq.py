def find_subsequences(nums):
    results = []
    dfs(nums, [], 0, results)
    return results

def dfs(nums, current, index, results):
    results.append(current[:])
    for i in range(index, len(nums)):
        current.append(nums[i])
        dfs(nums, current, i + 1, results)
        current.pop()


nums = [1, 2, 3, 4]
print(find_subsequences(nums))