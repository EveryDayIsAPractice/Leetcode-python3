class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        [M, CM, D, CD, C, XC, L, XL, X, IX, V, IV, I]=[0]*13

        if "M" in s:
            if "CM" in s:
                CM=1
                C-=1
                M-=1
            for count in range(len(s)):
                if s[count]=="M":
                    M+=1
        if "D" in s:
            if "CD" in s:
                CD=1
                C-=1
            else:
                D=1

        if "C" in s:
            if "XC" in s:
                XC=1
                X-=1
                C-=1
            for count in range(len(s)):
                if s[count]=="C":
                    C+=1
        if "L" in s:
            if "XL" in s:
                XL=1
                X-=1
            else:
                L=1

        if "X" in s:
            if "IX" in s:
                IX=1
                I-=1
                X-=1
            for count in range(len(s)):
                if s[count]=="X":
                    X+=1
        if "V" in s:
            if "IV" in s:
                IV=1
                I-=1
            else:
                V=1
        if "I" in s:
            for count in range(len(s)):
                if s[count]=="I":
                    I+=1
        return (M*1000+CM*900+D*500+CD*400+C*100+XC*90+L*50+XL*40+X*10+IX*9+V*5+IV*4+I)

#[M, CM, D, CD, C, XC, L, XL, X, IX, V, IV, I]=[0]*13

# I 1
# V 5
# X 10
# L 50
# C 100
# D 500
# M 1000
