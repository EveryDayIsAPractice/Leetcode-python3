class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<1:
            return False
        prime=[1,2,3,5]
        if num in prime:
            return True
        while num%2==0:
            num=num/2
        while num%3==0:
            num=num/3
        while num%5==0:
            num=num/5
        if num==1:
            return True
        else:
            return False
