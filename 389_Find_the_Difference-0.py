class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        output=""
        s_list=[]
        for i in s:
            s_list.append(i)
        for j in t:
            if j not in s_list:
                output+=j
            else:
                s_list.remove(j)
        return output
