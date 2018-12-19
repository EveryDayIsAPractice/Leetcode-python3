class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mapping=dict()
        inverse=dict()
        for i, ch in enumerate(s):
            if ch in mapping:
                if mapping[ch]!=t[i]:
                    return False
            elif t[i] in inverse:
                return False
            else:
                mapping[ch]=t[i]
                inverse[t[i]]=ch
        return True
