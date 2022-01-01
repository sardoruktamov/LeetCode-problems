class Solution(object):
    def lengthOfLastWord(self, s):
        nat = s.strip().split(' ')[::-1][0]  #strip() methodi boshi va oxirgi bo`sh joylarni o`chiradi
        w = nat
        if w:
            return len(w)
        else:
            return "0"