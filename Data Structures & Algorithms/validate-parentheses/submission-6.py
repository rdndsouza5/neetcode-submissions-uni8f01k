class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {'}':'{', ')':'(',']':'['}

        for i in s:
            if i in closeToOpen.values():
                stack.append(i)
            if i in closeToOpen:
                if not stack:
                    return False
                if stack[-1]==closeToOpen[i]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True