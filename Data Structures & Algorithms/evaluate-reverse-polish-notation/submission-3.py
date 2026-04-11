class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        mathset= {'+','-','*','/'}
        res = 0
        stack = []
        for i in tokens:
            print(stack)
            if i in mathset:
                b = stack.pop()
                a = stack.pop()
                if i == '*':
                    stack.append(b*a)
                elif i == '+':
                    stack.append(b+a) 
                elif i == '/':
                    stack.append(int(a/b))
                elif i == '-':
                    stack.append(a-b)
            else:
                stack.append(int(i))
        return stack.pop()