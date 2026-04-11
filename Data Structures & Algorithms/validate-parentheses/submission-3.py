class Solution:
    def isValid(self, s: str) -> bool:
        stack= []
        for i in s:
            if i in ['(','{','[' ]:
                stack.append(i)
            elif i in ['}',')',']']:
                if len(stack)==0:
                    return False
                char = stack.pop(-1)
                print(char, i)
                if char=='{' and i != '}':
                    return False
                if char=='(' and i != ')':
                    return False
                if char=='[' and i != ']':
                    return False
                
        return False if len(stack)>0  else True
                
