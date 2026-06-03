class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        p = {
            ']': '[',
            '}': '{',
            ')': '('
        }

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack or stack[-1] != p[ch]:
                    return False

                stack.pop()

        return len(stack) == 0