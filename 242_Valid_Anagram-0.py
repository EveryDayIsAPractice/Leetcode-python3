class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s is None:
            if t is None:
                return True
            else:
                return False
        elif t is None:
            return False
        memory=dict()
        memory2=dict()
        for i in s:
            if i in memory:
                memory[i]+=1
            else:
                memory[i]=1
        for i in t:
            if i in memory2:
                memory2[i]+=1
            else:
                memory2[i]=1
        if len(memory)!=len(memory2):
            return False
        for i in memory:
            if i in memory2:
                if memory[i]!=memory2[i]:
                    return False
            else:
                return False
        return True
