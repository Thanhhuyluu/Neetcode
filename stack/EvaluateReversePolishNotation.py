# https://neetcode.io/problems/evaluate-reverse-polish-notation/question?list=neetcode150
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(int(t))            
            else:
                temp = 0
                if t == "+":
                    temp = stack[-2] + stack[-1]
                elif t == "-":
                    temp = stack[-2] - stack[-1]
                elif t == "*":
                    temp = stack[-2] * stack[-1]
                else:
                    temp = stack[-2] / stack[-1]



                stack.pop()
                stack.pop()
                stack.append(int(temp))

        return stack[-1]
solution = Solution()
tokens = ["1","2","+","3","*","4","-"]
print(solution.evalRPN(tokens))
tokens=["4","13","5","/","+"]
print(solution.evalRPN(tokens))
