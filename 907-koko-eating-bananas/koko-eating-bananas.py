class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans=0
        low=1
        high=max(piles)

        while low<=high:
            mid=(low+high)//2

            t=0
            for p in piles:
                t+=(p+ mid - 1) // mid
            if t<=h:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans