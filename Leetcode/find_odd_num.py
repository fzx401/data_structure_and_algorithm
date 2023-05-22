"""一个数组中，只有一个数字出现了奇数次，其他数字都出现了偶数次，如何找到这个奇数次的数"""
def find_odd_num(nums: list):
    res = nums[0]
    for i in range(1, len(nums)):
        res = res ^ nums[i]
    return res

print(find_odd_num([1, 1, 2, 2, 3, 3, 4]))

"""一个数组中，有两个不同的数字出现了奇数次，其他数字都出现了偶数次，如何找到这两个奇数次的数"""
def find_odd_num2(nums: list):
    res = nums[0]
    for i in range(1, len(nums)):
        res = res ^ nums[i]
    #  此时的res为两个不同的出现了奇数次的数字之间的异或，res不为0，则某一位上必定为1
    res & (~res + 1)  # 提取出最右侧的1
    return res

print(find_odd_num2([1, 1, 2, 2, 3, 3, 4, 4, 5, 6]))