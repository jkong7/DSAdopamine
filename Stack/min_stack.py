class MinStack(object):
    #Cannot be that hard
    #Have a variable that keeps track of min 
    #Maybe keep track of two variables, one for min, and one for next min? 

    def __init__(self):
        self.stack=[]
        self.minn=float('inf')
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.minn=min(self.minn, val)
        self.stack.append((val, self.minn))
        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        if self.stack: 
            self.minn=self.stack[-1][1]
        else: 
            self.minn=float('inf')
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()