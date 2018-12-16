class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.sort_stack=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.sort_stack:
            insert_or_not=0
            for num, i in enumerate(self.sort_stack):
                if x<i:
                    self.sort_stack.insert(num,x)
                    insert_or_not=1
                    break
            if insert_or_not==0:
                self.sort_stack.append(x)
        else:
            self.sort_stack.append(x)
        self.stack.append(x)

        

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.sort_stack.remove(self.stack[-1])
            del self.stack[-1]
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        else:
            return None
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.sort_stack:
            return self.sort_stack[0]
        else:
            return None
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
