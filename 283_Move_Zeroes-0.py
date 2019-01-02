class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        pre = 0
        for i, num in enumerate(nums):
            if num != 0:
                if pre<i :
                    nums[pre] = num
                    nums[i] = 0
                pre += 1
