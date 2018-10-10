class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words=s.split()
        if len(words):
            return len(words[-1])
        else:
            return 0

