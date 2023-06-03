from find_distinct_subseq import find_subsequences

def find(nums, target):
    total = find_subsequences(nums)
    tmp = [sum(i) for i in total]
    i = 0
    while i < len(tmp):
        if tmp[i] == target:
            return total[i]
        i += 1

nums = [1, 2, 3, 4, 6]
target = 13
print(find(nums, target))