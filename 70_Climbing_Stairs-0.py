class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        save = dict()
        def climb(n)
            if n in save:
                return save[n]
            if n < 0:
                return None
            elif n==1:
                save[n]=1
                return 1
            elif n==2:
                save[n]=2
                return 2
            else:
                save[n] = climb(n-1) + climb(n-2)
                return save[n]
        return climb(n)
