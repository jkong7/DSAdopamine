class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #Competitive just means smaller number lmao 
        #Same length (smallest numebr of length k??) 
        #How many to remove=len(nums)-k 
        #Greedy remove next less (mono increasing stack)
        #If not k operations, remove last (remaining k) elements from stack 
        #Because no pop means that those last elements are strictly greater 
        #than prev elements so we want to remove those to minimize the number 
        #For example, strictly increasing pattern: 12345 
        #1. Basically, any DIPS, we remove the greater element greedily/immediately
        #so we use mono stack to do next less 
        #2. If strictly increasing pattern, we remove from the ends (since those are
        #larger)
        remove=len(nums)-k
        stack=[]
        for num in nums: 
            while remove and stack and num<stack[-1]: 
                stack.pop()
                remove-=1 
            stack.append(num)
        stack=stack[:len(stack)-remove] #Remove last 'remove' elements (case for when
        #remove isn't 0, increasing pattern remove the ends!)
        return stack 
        #O(2n)->O(n) (each element pushed and popped once)

        