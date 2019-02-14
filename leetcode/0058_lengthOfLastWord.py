class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.rstrip()
        n = s.rfind(' ')
        l = len(s)
        if n < 0:
            return l
        else:
            return l - n - 1