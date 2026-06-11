# https://neetcode.io/problems/string-encode-and-decode/history?submissionIndex=5
from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded +=(str(len(s)) + "#" + s)
        return encoded
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            result.append(s[j+1 : j+1+length])

            i = j + 1 + length
        return result

            

s = Solution()

encode_result = s.encode(["Hello","World"])
print(encode_result)
decode_result = s.decode(encode_result)
print(decode_result)

