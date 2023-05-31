class ReversePair:
    def __init__(self):
        self.reverse_pair_count = 0

    def reverse_pair(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        left = self.reverse_pair(left)
        right = self.reverse_pair(right)

        i, j, res = 0, 0, []
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                self.reverse_pair_count += len(right) - j
                res.append(right[j])
                j += 1
            else:
                res.append(left[i])
                i += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res

s = ReversePair()
arr = [7,5,6,4]
s.reverse_pair(arr)
print(s.reverse_pair_count)