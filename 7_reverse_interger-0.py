class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        elif x > 0:
            temp = x
            x_reverse = []
            new = 0
            while(temp>=10):
                final = temp%10
                # note!!!!!
                if final!=0 or len(x_reverse)!=0:
                    x_reverse.append(final)
                # note!!!!!
                temp = (temp-final)/10
            x_reverse.append(temp)
            for count in range(len(x_reverse)):
                new = new + x_reverse[-(1+count)]*(10**count)
            if new >= 2**31:
                return 0
            else:
                return int(new)
        else:
            temp = -1*x
            x_reverse = []
            new = 0
            while(temp>=10):
                final = temp%10
                if final!=0 or len(x_reverse)!=0:
                    x_reverse.append(final)
                temp = (temp-final)/10
            x_reverse.append(temp)
            for count in range(len(x_reverse)):
                new = new + x_reverse[-(1+count)]*(10**count)
            if new > 2**31:
                return 0
            else:
                return int(-1*new)
