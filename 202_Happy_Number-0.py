class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==1:
            return True
        temp=[n]
        while n!=1:
            happy=(n%10)*(n%10)
            res=int(n/10)
            while res>0:
                happy+=(res%10)*(res*10)
                res=int(res/10)
            if happy in temp:
                return False
            elif happy==1:
                return True
            else:
                n=happy
                temp.append(n)))
