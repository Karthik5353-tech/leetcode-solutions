class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1=set()
        left=0
        max_len=0

        for i in range (len(s)):
            while s[i] in s1:
                s1.remove(s[left])
                left+=1
            s1.add(s[i])

            max_len =max(max_len,i-left+1)
        return max_len