class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=[i.lower() for i in s if i.isalnum()]
        if s:
            for i in range(int(len(s)/2)):
                if s[i]!=s[-1-i]:
                    return False
            return True
        return True
