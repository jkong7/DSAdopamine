class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Keep small i values as far left as possible
        #Mono decreasing stack of i values 

        #Then go right to left and compare right element with top of stack, if it
        #is greater than or equal to top, that is the MAX distance between that 

        #Fill up a mono decreasing
        stack=[]
        for i in range(len(nums)): 
            if not stack or nums[stack[-1]]>nums[i]: 
                stack.append(i)
        
        #Go backwards and compare widths 
        best=0 
        for j in range(len(nums)-1, -1, -1): 
            while stack and nums[j]>=nums[stack[-1]]: 
                index=stack.pop()
                best=max(best, j-index)
        return best 


        #The reason we use mono decreasing stack is because if a number is larger
        #than the last element, then the max width will ALWAYS be used with the 
        #prev number instead, so that larger element has no use to us 
        #But if a number is to the right and LESS than, then there is potentially
        #a future number in between the values of top and less than which forms
        #the max width with the less than. 
        #So in one pass from left to right, we only care about numbers in decreasing
        #order, anything increasing has no utility 

        #And then we compare starting from the right (which maximizes width), we see
        #if larger/= than top of stack (in which case that forms a valid width) 
        #and we can pop that stack number because that width combo right there is 
        #the largest possible width with that stack index because then we would move
        #left in our loop and that would just form a smaller width 
        #And the popping is while num>stack[-1] and that retrieves the widest pos
        #ramp width with that loop number, after that we've calcualted the max width
        #with that loop number and those popped off stack numbers and then we can 
        #move left in our loop and compare with the remaining stack elements. 