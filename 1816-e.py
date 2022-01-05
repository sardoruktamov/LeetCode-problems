class Solution(object):
    def truncateSentence(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = s.split(" ")
        list = []
        result = " "
        for i in range(k):
            list.append(s[i])
            result.join(s[i])
        return (result.join(list))

## kodli test qilish qismi
# def isAnagram(s,k):
#     s = s.split(" ")
#     list = []
#     result = " "
#     for i in range(k):
#         list.append(s[i])
#         result.join(s[i])
#     return (result.join(list))
#
# s = "chopper is not a tanuki"
# k = 5
# a = isAnagram(s,k)
# print(a)