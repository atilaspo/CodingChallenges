class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            if item == "+":
                calculation = stack.pop() + stack.pop()
                stack.append(calculation)
            elif item == "-":
                a, b = stack.pop(), stack.pop()
                calculation = b - a
                stack.append(calculation)
            elif item == "*":
                a, b = stack.pop(), stack.pop()
                calculation = a * b
                stack.append(calculation)
            elif item == "/":
                a, b = stack.pop(), stack.pop()
                calculation = b / a
                stack.append(int(calculation))
            else:
                stack.append(int(item))
        return stack[-1]