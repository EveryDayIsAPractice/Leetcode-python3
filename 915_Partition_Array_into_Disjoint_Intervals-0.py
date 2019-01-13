class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        output = 1
        left_max = A[0]
        temp_max = A[0]
        end = False
        while not end:
            shift=1
            for i in A[output:]:
                if i>temp_max:
                    temp_max=i
                if i<left_max:
                    output+=shift
                    left_max=temp_max
                    end = False
                    break
                else:
                    shift+=1
                    end = True
        return output
