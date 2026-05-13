class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def backtrack(s,openp,closep):
            if len(s)==2*(n):
                result.append(s)
                return 
            if openp < n:
                backtrack(s + "(", openp + 1, closep)
            if closep < openp:
                backtrack(s + ")", openp, closep + 1)

        backtrack("", 0, 0)

        return result
