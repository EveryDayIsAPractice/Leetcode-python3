class Solution:
    def maxProfit(self, prices):
        """"
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        min=prices[0]
        max=0
        pro=0
        for i in prices:
            if i<min:
                min=i
                max=0
            elif i > max:
                max=i
            if max-min > pro:
                pro=max-min
        return pro

