import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "").lower()
        s = re.sub("[^a-zA-Z0-9]", "", s)
        for i in range(len(s)//2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

        