def find_odd_num(nums: list):
    res = nums[0]
    for i in range(1, len(nums)):
        res = res ^ nums[i]
    return res


print(find_odd_num([1, 1, 2, 2, 3, 3, 4]))
