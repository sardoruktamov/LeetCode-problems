
class Solution(object):
    def isAnagram(self, s, t):
        s = "".join(sorted(list(s)))
        t = "".join(sorted(list(t)))

        return s==t






# def isAnagram(s,t):
#
#     # nat = list(s)
#     # sort = sorted(list(s))
#     s = "".join(sorted(list(s)))
#     t = "".join(sorted(list(t)))
#     return t == s
#
# a = isAnagram("rat", "car")
#
# print(a)
