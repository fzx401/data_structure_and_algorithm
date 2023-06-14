class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1| n == 2:
            return n
        num_n_1, num_n_2 = 2, 1
        for i in range(3, n+1):
            current = num_n_1 + num_n_2
            num_n_2 = num_n_1
            num_n_1 = current
        return current

s = Solution()
print(s.climbStairs(5))