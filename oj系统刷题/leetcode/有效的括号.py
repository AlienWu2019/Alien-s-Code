class Solution:
    def isValid(self, s: str) -> bool:
        keys = {"(": ")", "[": "]", "{": "}"}
        stack = list()
        for i in range(len(s)):
            if s[i] in keys:
                stack.append(s[i])
            else:
                if len(stack) == 0: #考虑只有一个右括号的情况
                    return False
                if keys[stack.pop()] != s[i]:
                    return False
        if len(stack) != 0: #考虑只有一个左括号的情况
            return False
        return True




a = Solution()
print(a.isValid("]"))

