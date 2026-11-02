class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears    more than once in the array, otherwise return false. 
        """
        dict_soluciones = {}
        for i in nums:
            if i in dict_soluciones.keys():
                dict_soluciones[i] += 1
                return True
            else:
                dict_soluciones[i] = 1
        return False