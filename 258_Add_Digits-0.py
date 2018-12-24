class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        total=num
        while total>=10:
            res=total
            total=0
            while res>=10:
                total+=res%10
                res=int(res/10)
            total+=res
        return total
