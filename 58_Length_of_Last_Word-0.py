class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words=s.split()
        #if len(words):
        #    return len(words[-1])
        #else:
        #    return 0
        return len("".join(words[-1:]))
        # it is faster than if/else
        # use [-1:] to prevent out of list
        # use "".join to prevent wrong length
