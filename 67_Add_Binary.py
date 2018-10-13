class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        value_a=dict()
        value_b=dict()
        value_temp=dict()
        value_temp[0]=0
        output=""
        for i in range(len(a)):
            value_a[i] = int(a[-1-i])
        for i in range(len(b)):
            value_b[i] = int(b[-1-i])
        value_c = value_a if (len(a)>len(b)) else value_b
        max = len(a) if (len(a)>len(b)) else len(b)
        min = len(a) if (len(a)<len(b)) else len(b)
        for i in range(min):
            if value_temp[i] + value_a[i] + value_b[i] == 1:
                value_temp[i] = 1
                value_temp[i+1] = 0
            elif value_temp[i] + value_a[i] + value_b[i] == 2:
                value_temp[i] = 0
                value_temp[i+1] = 1
            elif value_temp[i] + value_a[i] + value_b[i] == 3:
                value_temp[i] = 1
                value_temp[i+1] = 1
            else:
                value_temp[i+1] = 0
        if max-min > 0:
            for i in range(min, max):
                if value_temp[i] + value_c[i] == 1:
                    value_temp[i]=1
                    value_temp[i+1] = 0
                elif value_temp[i] + value_c[i] == 2:
                    value_temp[i] = 0
                    value_temp[i+1] = 1
                else:
                    value_temp[i+1] = 0
        for i in range(len(value_temp)):
            j = len(value_temp)-i-1
            if value_temp[j]==0 and output =="" and j!=0:
                continue
            else:
                output += str(value_temp[j])
        return output
