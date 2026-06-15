# https://neetcode.io/problems/is-palindrome/question?list=neetcode150
class Solution:
    def isPalindrome(self, s: str) -> bool:
        norm = "".join(s.lower().split())
        temp = []
        for n in norm:
            if (n.isdigit() or n.isalpha()):
                temp.append(n)
        i = 0
        j = len(temp)-1


        while i < j:
            if temp[i] != temp[j]: 
                return False
            i += 1
            j -= 1
        return True
solution = Solution()
s = "Was it a car or a cat I saw?"
print(solution.isPalindrome(s))

s = "tab a cat"
print(solution.isPalindrome(s))

