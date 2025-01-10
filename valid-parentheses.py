class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        is_closing_key = { ")" : "(", "}" : "{", "]" : "[" }

        for ch in s:
            if ch in is_closing_key:
                if stack and stack[-1] == is_closing_key[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return len(stack) == 0