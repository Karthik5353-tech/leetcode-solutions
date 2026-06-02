class Solution:
    def earliestFinishTime(self, lst: List[int], ldu: List[int], wst: List[int], wdu: List[int]) -> int:

        ans=float("inf")

        for i in range(len(lst)):
            t=lst[i]+ldu[i]
            for j in range(len(wst)):
                ans=min(ans, max(t,wst[j])+wdu[j])

        for i in range(len(wst)):
            t=wst[i]+wdu[i]
            for j in range(len(lst)):
                ans=min(ans,max(t,lst[j])+ldu[j])
        return ans
        