class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                a , b = stack.pop() , stack.pop()
                res = b - a
                stack.append(res)
            elif i == "*": 
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                a , b = stack.pop() , stack.pop()
                res = int(b / a)
                stack.append(res)
            else:
                stack.append(int(i))
        return stack[0]