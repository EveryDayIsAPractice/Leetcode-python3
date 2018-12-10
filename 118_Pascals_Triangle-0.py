class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output=[]
        if numRows<1:
            return output
        else:
            output.append([1])
            # for numRows>=2
            for i in range(numRows-1):
                temp=[1]*(i+2)
                #for numRows >=3
                for j in range(i):
                    temp[j+1]=output[-1][j]+output[-1][j+1]
                output.append(temp)
            return output
