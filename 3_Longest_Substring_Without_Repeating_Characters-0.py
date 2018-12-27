class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        memory=[]
        length=0
        for i in s:
            if i in memory:
                if len(memory)>length:
                    length=len(memory)
                index=memory.index(i)
                memory=memory[(index+1):]
            memory.append(i)
        if len(memory)>length:
            length=len(memory)
        return length
