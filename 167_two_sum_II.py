class Solution:
    def twoSum(self, numbers, target):
        """
        num: List[int]
        target: int
        rtype: List[int]
        Note: index is one-based, not zero-based
        """
        if len(numbers)==1:
            return None
        diff=dict()
        for i, num in enumerate(numbers):
            diff[target-num]=i+1
        for i, num in enumerate(numbers):
            if num in diff:
                if i+1 > diff[num]:
                    return [diff[num],i+1]
                else:
                    return [i+1,diff[num]]
        return None
