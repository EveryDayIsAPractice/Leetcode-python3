## modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=None
        i=0
        while i < len(nums):
            if nums[i]==temp:
                nums.remove(nums[i])
            else:
                temp=nums[i]
                i+=1
        return len(nums)

#nums=[0,0,1,1,1,2,2,3,3,4]
#Solution.removeDuplicates(None, nums)
#for i in range(Solution.removeDuplicates(None, nums)):
#    print(nums[i])

#print(Solution.removeDuplicates([1,1,2]) )

## the returned value is an integer but your answer is an array

## You can think of it
# nums is passed in by reference. (i.e., without making a copy)
#int len = removeDuplicates(nums);
#
# any modification to nums in your function would be known by the caller.
# using the length returned by your function, it prints the first len elements.
#for (int i = 0; i < len; i++) {
#            print(nums[i]);
#            }
