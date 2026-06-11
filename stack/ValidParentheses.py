# neetcode.io/problems/validate-parentheses/question?list=neetcode150
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        for temp in s:
            if temp in dict and stack:
                a = stack.pop()
                if a != dict[temp]:
                    return False

            else:
                stack.append(temp)
            
        return len(stack) == 0
            
                

solution = Solution()

s = "("
print(solution.isValid(s))
