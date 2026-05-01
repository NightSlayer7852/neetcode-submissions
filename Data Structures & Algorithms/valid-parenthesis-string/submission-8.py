class Solution:
    def checkValidString(self, s: str) -> bool:
        stack1, stack2 = [], []

        for i, c in enumerate(s):
            if c == "(":
                stack1.append(i)
            elif c == ")":
                if not stack1 and not stack2:
                    return False
                if stack1:
                    stack1.pop()
                elif stack2:
                    stack2.pop()
            else:
                stack2.append(i)
        while stack1 and stack2 and stack1[-1] < stack2[-1]:
            stack1.pop()
            stack2.pop()
        return len(stack1) == 0