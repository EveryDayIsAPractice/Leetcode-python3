class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        new=""
        for i in s:
            new = i + new
        return new
