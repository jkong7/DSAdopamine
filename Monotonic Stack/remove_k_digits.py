class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        #First observation: Removing k digits from num will always give you a number
        #with len(nums)-k digits. So obviously we want to minimize first digit 

    
        #Mono increasing stack? 
        #Finds next less element. When invariant breaks, pop top of the stack, that 
        #pop is what you WANT TO REMOVE
        #Its greedy, for example 43..., 3<4 so you pop 4. No matter what follos 43, 
        #popping 4 will always be more optimal than popping 3.  
        #Traverse linearly and if invariant breaks, pop immediately, 
        #Every time you pop, decrement k, if k reaches 0, CANT POP ANYMORE, so 
        #elements proceeding this will just be pushed onto stack, the stack 
        #from bottom to top will make up the output integer

        stack=[]
        for number in num: 
            while k!=0 and stack and int(number)<int(stack[-1]): 
                stack.pop()
                k-=1 
            stack.append(number)
        stack=stack[:len(stack)-k]
        result="".join(stack)
        return str(int(result)) if result else '0'
        #That trick above (converting to int and then back to string) gets rid of
        #leading zeroes. If k elements didnt get popped, we pop the last k elements
        #(however much of k is left). For example increasing 12345, nothing gets pop
        #but we want to take the last elements out to minimize integer and 
        #stack=stack[:len(stack)-k] does this, note no effect if k=0. 
        #At its core, its just a next less element mono increasing stack problem that
        #is greedy