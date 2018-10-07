class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle==None:
            return 0
        elif needle not in haystack:
            return -1
        else:
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i:i+len(needle)] == needle:
                    return i

#What should we return when needle is an empty string?
#This is a great question to ask during an interview.

#For the purpose of this problem,
#we will return 0 when needle is an empty string.
