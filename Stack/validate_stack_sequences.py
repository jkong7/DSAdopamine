class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """

        i=0 
        stack=[]
        for index in range(len(pushed)+1):
            while stack and stack[-1]==popped[i]: 
                i+=1 
                stack.pop()
            if index<len(pushed): 
                stack.append(pushed[index])
        return not stack 

        #And yeah if stack is empty it means everything cancelled out and the pops matche
        #the pushes so thats true

        #You dont even run into that problem if you just append first and then stack
        i=0 
        stack=[]
        for index in range(len(pushed)):
            stack.append(pushed[index])
            while stack and stack[-1]==popped[i]: 
                i+=1 
                stack.pop()
        return not stack 