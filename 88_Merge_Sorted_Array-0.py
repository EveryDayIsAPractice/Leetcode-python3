class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        now = 0
        for i in nums2:
            while True:
                if now==m:
                    nums1.insert(now,i)
                    del nums1[-1]
                    now +=1
                    m +=1
                    break
                if nums1[now]<i:
                    now+=1
                else:
                    nums1.insert(now,i)
                    del nums1[-1]
                    now +=1
                    m +=1
                    break
