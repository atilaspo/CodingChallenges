class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def back_track(openP, closeP):
            if openP == closeP == n:
                res.append(''.join(stack))
                return

            if openP < n:
                stack.append("(")
                back_track(openP + 1, closeP)
                stack.pop()
            if closeP < openP:
                stack.append(")")
                back_track(openP, closeP + 1)
                stack.pop()
        
        back_track(0,0)
        return res