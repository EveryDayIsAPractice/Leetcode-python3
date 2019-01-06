class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd=[]
        even=[]
        for num in A:
            if num%2==0:
                even.append(num)
            else:
                odd.append(num)
        for i in range(len(odd)):
            even.insert(2*i+1, odd[i])
        return even
