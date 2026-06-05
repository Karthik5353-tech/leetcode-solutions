class Solution:
    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        ans = [-1, -1]
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                ans[0] = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                ans[1] = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return ans