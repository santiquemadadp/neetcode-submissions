class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return True if the two are anagrams of each other, otherwise return False
        """
        s_list = []
        t_list = []
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_list.append(s[i])
            t_list.append(t[i])
        return sorted(s_list) == sorted(t_list)

        