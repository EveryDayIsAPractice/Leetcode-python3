class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.accumulation = [0]*len(nums)
        for i,j in enumerate(nums):
            if i==0:
                self.accumulation[0] = nums[0]
            else:
                self.accumulation[i] = self.accumulation[i-1] + j
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==0:
            return self.accumulation[j] 
        else:
            return self.accumulation[j] - self.accumulation[i-1] 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
