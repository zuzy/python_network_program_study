class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        ca = 0
        cb = 0
        r = ''
        while A > 0 or B > 0:
            if A == 0 and B == 0:
                return r
            if cb >= 2:
                r += 'a'
                A -= 1
                ca += 1
                continue
            elif ca >= 2:
                r += 'b'
                B -= 1
                cb += 1
                continue
            if A > B:
                r += 'a'
                A -= 1
                ca += 1
            else:
                r += 'b'
                B -= 1
                cb += 1
            
        return r
            
