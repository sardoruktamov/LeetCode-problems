class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result


## kodli test qilish qismi
# def isAnagram(nums, n):
#     result = []
#     for i in range(n):
#         result.append(nums[i])
#         result.append(nums[i+n])
#     return result
#
#
# nums = [2,5,1,3,4,7]
# n = 3
# a = isAnagram(nums, n)
#
# print(a)
