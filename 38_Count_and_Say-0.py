class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return "1"
        else:
            seq=self.countAndSay(n-1)
            temp=None
            output=""
            count=dict()
            for num in seq:
                if num!=temp:
                    if temp==None:
                        temp=num
                        count[num]=1
                    else:
                        output = output+ str(count[temp]) + temp
                        temp=num
                        count[num]=1
                else:
                    count[temp]+=1
            output = output+ str(count[temp]) + temp
            return output

# Note: 1 -> 1
# 2 -> countAndSay(1) = 11
# 3 -> countAndSay(11) = 21
# 4 -> countAndSay(21) = 1211


