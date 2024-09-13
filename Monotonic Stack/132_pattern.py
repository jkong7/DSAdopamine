class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #Find prev greater, keep track of min value so far 
        #Once found prev greater, if element greater than min, return true, 
        #min works because if its not even greater than min, it wont be greater 
        #than anything else on the left so there is no i value
        #i is being minimized with one variable 
        #k is being maximized using stack 
        #Mono decreasing 

        stack=[]
        minn=float('inf')
        for i in range(len(nums)): 
            while stack and nums[i]>=nums[stack[-1][0]]: #Index/min up to 
                stack.pop()
            if stack: 
                if nums[i]>stack[-1][1]: #> than top of stack min up to
                    return True 
            stack.append((i, minn)) #minn up to i is being stored/appended 
            minn=min(minn, nums[i])
        return False 
        #I got it! Just needed the check to be >= not just >

        #Summary: Use a mono decreasing stack to find prev greater element 
        #Once we are here, we know that we have found 3>2, then compare 2 
        #with the MINIMUM value in the array up to the 3. We store min up to 
        #by storing it alongside the index/value in the stack and access it 
        #with stack[1]. So if 2/nums[i]>min up to 3/1/stack[-1][1], then return 
        #true (note that inside the if stack statement, it means the invariant
        #for mono decreasing is repaired/good to go and that we have found the
        #3>2 so we must just check for 2>1). Then obviously append to stack the 
        #index and the minn which is calculated AFTER this (min up to value)
        #Its also >= not just > bc invariant isnt true when = (3>2 cant hold true 
        #equal)
