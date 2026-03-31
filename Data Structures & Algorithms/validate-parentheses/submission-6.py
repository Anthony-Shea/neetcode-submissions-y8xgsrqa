class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 1:
            return False
        if s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            elif stack:
                check = stack.pop()
                if char == ")" and check != "(":
                    return False
                if char == "}" and check != "{":
                    return False
                if char == "]" and check != "[":
                    return False
            else:
                return False
        if not stack:
            return True
        return False
