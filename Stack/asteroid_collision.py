class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        #Maybe keep a mono increasing stack and if the processed value is negative,
        #compare abs value to top of the stack, if less than, it destroys itself, 
        #if greater than, everything in the stack is destroyed 

        #So every negative value triggers something for everything to its left 
        #and itself before moving on to the next value 
        #So stack will only contain the positive values? 
        #negative, positive NOTHING HAPPENS
        #So only when you compare a negative to a stack (positive, negative pattern)
        #does something happen


        #Negative value and stack is empty-append value 

        #Negative value, if it is greater than top of the stack, pop everything in 
        #the stack WITHOUT appending 

        #Yeah negative value, compare it against every single top, if greater, pop
        #without appending. If it pops EVERYTHING in the stack, append that neg
        #value to the result, OTHERWISE, it got destroyed by a positive value so 
        #DONT append it 
        #Okay, AFTER every element has been processed, ANYTHING LEFT IN THE STACK
        #are VALID positive values so append all of those to the result in order 
        #left to right 
        #So for negative, use the while nums[i]>stack[-1] and then outside that 
        #while loop, only if stack is empty do you append the negative value to 
        #result 
        #If positive value, just append to stack 

        #If negative value and = to top of stack, pop and then DONT append, so prob
        #use a continue 



        stack=[]
        result=[]
        for size in asteroids: 
            if size>0: 
                stack.append(size)
                continue 
            abs_size=abs(size)
            while stack and abs_size>stack[-1]: 
                stack.pop()
            #Means neg got stopped, if it got stopped by the same value, simply pop
            #that top and continue (nothing gets appended): 
            if stack and abs_size==stack[-1]: 
                stack.pop()
                continue
            #Otherwise if stack empty, neg broke all the positives, that means its
            #still alive and we append it (also for when no pos values are even
            #appended to stack so neg values just freely stay alive)
            if not stack: 
                result.append(size)
            #If stack not empty, means neg got stopped and destroyed, so nothing
            #appended
        #Remaining pos stack values didn't get destroyed so those get appended 
        for size in stack: 
            result.append(size) #Note: Negatives will all be on left to positives
        return result 
