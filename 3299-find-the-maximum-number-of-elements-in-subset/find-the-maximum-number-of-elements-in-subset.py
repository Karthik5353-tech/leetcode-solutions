from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = cnt[1] if cnt[1] % 2 else cnt[1] - 1

        for x in cnt:
            if x == 1:
                continue

            cur = x
            length = 0

            while cnt[cur] > 1:
                length += 2
                cur *= cur

            ans = max(ans, length + (1 if cnt[cur] else -1))

        return ans