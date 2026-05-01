class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for x in s:
            if x =='(' or x == '{' or x == '[':
                stack.append(x)
            elif x ==')' and stack and stack[-1] == '(':
                stack.pop(-1)
            elif x =='}' and stack and stack[-1] == '{':
                stack.pop(-1)
            elif x ==']' and stack and stack[-1] == '[':
                stack.pop(-1)
            else:
                return False
        return len(stack)==0