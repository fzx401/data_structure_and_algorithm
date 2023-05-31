class ReversePair:
    def reverse_pair(self, nums):
        if len(nums) <= 1:
            return nums, 0
        mid = len(nums) // 2
        left, left_count = self.reverse_pair(nums[:mid])
        right, right_count = self.reverse_pair(nums[mid:])

        i, j, res = 0, 0, []
        count = left_count + right_count
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                count += len(right) - j
                res.append(right[j])
                j += 1
            else:
                res.append(left[i])
                i += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res, count

s = ReversePair()
arr = [7, 5, 6, 4]
_, reverse_pair_count = s.reverse_pair(arr)
print(reverse_pair_count)


