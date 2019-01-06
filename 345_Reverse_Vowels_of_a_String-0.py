class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        new=[]
        position=[]
        count=0
        for j, i in enumerate(s):
            new.append(i)
            if i in vowels:
                position.append(j)
        for j, i in enumerate(position):
            new[i] = s[position[-1-j]]
        new = "".join(new)
        return new
