class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i not in "+-*/":
                stack.append(int(i))
            else:
                l = int(stack.pop())
                r = int(stack.pop())
                if i == '+':
                    stack.append(l+r)
                elif i == '-':
                    stack.append(r-l)
                elif i == '*':
                    stack.append(r*l)
                elif i == '/':
                    if(l == 0):
                        stack.append(0)
                    else:
                        stack.append(r/l)
        return int(stack.pop())
