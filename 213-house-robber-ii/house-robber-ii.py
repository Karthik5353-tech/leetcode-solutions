class Solution:
    
    def helper(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[n - 1]

    def rob(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]

        case1 = self.helper(nums[:-1])
        case2 = self.helper(nums[1:])

        return max(case1, case2)