class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int"
        :rtype: List[int]
        """""
        output=[1]
        for i in range(rowIndex):
            output.append(1)
            temp1=1
            for j in range(1,i+1):
                temp2=output[j]
                output[j]=temp1+temp2
                temp1=temp2
        return output
