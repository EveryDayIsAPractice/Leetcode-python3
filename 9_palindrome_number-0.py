class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<10 and x >=0 :
            return True
        elif x >= 10:
            x_str = str(x)
            for count in range(int(len(x_str)/2)):
                if x_str[count] != x_str[-(1+count)]:
                    return False
            return True
        else:
            return False






        # palindrome 迴文
        # positive example: 121
        # negative example: -121, 10
