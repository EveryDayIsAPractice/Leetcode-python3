#Do not allocate extra space for another array,
#you must do this by modifying the input array in-place
#with O(1) extra memory. O(1) EXTRA MEMORY!

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        while i<len(nums):
            if nums[i]==val:
                nums.remove(val)
            else:
                i+=1
        return len(nums)

#nums = [3,2,2,3]
#val = 3
#
#for i in range(Solution.removeElement(None, nums, val):
#    print(nums[i])
