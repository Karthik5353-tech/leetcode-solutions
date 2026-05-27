class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        total=0
        max_len=float('inf')

        for right in range(len(nums)):
            total+=nums[right]

            while total>=target:
                    max_len=min(max_len,right-left+1)
                    total-=nums[left]
                    left+=1
        return 0 if max_len == float('inf') else max_len