class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        tmp = set(['*','+','-','/'])
        for i in tokens:
            if i not in tmp:
                stack.append(int(i))
            elif i=='-':
                a= stack.pop()
                b = stack.pop()
                res = b-a
                stack.append(res)
            elif i=='+':
                a= stack.pop()
                b = stack.pop()
                res = b+a
                stack.append(res)
            elif i=='*':
                a= stack.pop()
                b = stack.pop()
                res = b*a
                stack.append(res)
            elif i=='/':
                a= stack.pop()
                b = stack.pop()
                res = int(b/a)
                stack.append(res)
        return stack.pop()