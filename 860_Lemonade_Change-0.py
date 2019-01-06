class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        change={5:0,10:0,20:0}
        for i in bills:
            change[i]+=1
            if i==10:
                if change[5]<1:
                    return False
                else:
                    change[5]-=1
            elif i==20:
                if change[10]<1:
                    if change[5]<3:
                        return False
                    else:
                        change[5]-=3
                else:
                    if change[5]<1:
                        return False
                    else:
                        change[5]-=1
                        change[10]-=1
        return True
