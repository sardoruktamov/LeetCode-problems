class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        dot = "[.]"
        for i in address:
            if i == ".":
                r = address.replace(".", dot)
                return r

# ## kodli test qilish qismi
# def isAnagram(address):
#
#     dot = "[.]"
#     for i in address:
#         if i == ".":
#             r = address.replace(".", dot)
#             return r
#
#
# address = "1.1.1.1"
# a = isAnagram(address)
#
# print(a)