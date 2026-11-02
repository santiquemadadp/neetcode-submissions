class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return True if the two are anagrams of each other, otherwise return False
        """
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

        