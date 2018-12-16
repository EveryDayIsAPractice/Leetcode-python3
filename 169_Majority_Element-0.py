class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length_half=len(nums)/2
        if length_half:
            count=dict()
            for i, num in enumerate(nums):
                if num in count:
                    count[num]+=1
                    if count[num]>length_half:
                        return num
                else:
                    count[num]=1
        else:
            if nums:
                return nums[0]
            else:
                return None
