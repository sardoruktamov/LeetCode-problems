class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        import math
        result = int(math.floor(math.sqrt(x)))
        return result



# import math
# ## kodli test qilish qismi
# def isAnagram(x):
#     result = int(math.floor(math.sqrt(x)))
#     return result
#
#
# x = 8
# a = isAnagram(x)
#
# print(a)