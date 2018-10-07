class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            return nums.index(target)
        else:
            if target < nums[0]:
                return 0
            if len(nums)==1:
                return 1
            for i in range(len(nums)-1):
                if nums[i]< target and nums[i+1]>target:
                    return i+1
            return len(nums)

