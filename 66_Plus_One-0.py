class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits):
            if digits[-1]!=9:
                digits[-1]+=1
                return digits
            else:
                digits[:-1] = self.plusOne(digits[:-1])
                digits[-1]=0
                return digits
        else:
            return [1]

