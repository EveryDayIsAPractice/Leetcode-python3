class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=n
        output=0
        while res>=5:
            res = int(res/5)
            output += res
        return output
