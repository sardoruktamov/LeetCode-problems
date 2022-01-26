
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jivel = []
        for i in jewels:
            jivel.append(i)
        stone = []
        for i in stones:
            stone.append(i)

        jiv_num = 0
        for m in stone:
            for n in jivel:
                if n in m:
                    jiv_num += 1
        return int(jiv_num)




# # ## kodli test qilish qismi
# def isAnagram(j,s):
#     jivel = []
#     for i in j:
#         jivel.append(i)
#     stone = []
#     for i in s:
#         stone.append(i)
#
#     jiv_num = 0
#     for m in stone:
#         for n in jivel:
#             if n in m:
#                 jiv_num += 1
#     return int(jiv_num)
#
# x = 'aA'
# y = 'aAAbbAb'
# a = isAnagram(x,y)
#
# print(a)