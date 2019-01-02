class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split()
        if len(str_list) != len(pattern):
            return False
        memory = dict()
        verify = []
        for i, word in enumerate(str_list):
            if word in memory:
                if memory[word] != pattern[i]:
                    return False
            else:
                if pattern[i] in verify:
                    return False
                else:
                    memory[word] = pattern[i]
                    verify.append(pattern[i])
        return True
