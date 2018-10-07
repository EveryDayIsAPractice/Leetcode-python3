class Solution:
    def twoSum(self, nums, target):
        """
        num: List[int]
        target: int
        rtype: List[int]
        """
        if len(nums)==1:
            return None

        for i, num in enumerate(nums):
## useless for there may negative add negative
#            if num>target:
#                continue
            for count in range(i+1, len(nums)):
                if (num + nums[count]) == target:
                    return [i, count]
        return None
