class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def condition(capacity): 
            D=1 
            total=0
            for weight in weights: 
                total+=weight 
                if total>capacity: 
                    total=weight 
                    D+=1 
                    if D>days: 
                        return False  
            return True  #O(n) loop, #O(1) work done in each loop, total: O(n)
        
        left, right=max(weights), sum(weights)
        while left<right: 
            mid=left+(right-left)//2 
            if condition(mid): 
                right=mid 
            else: 
                left=mid+1 
        return left #O(log(sum(weights)-max(weights)))

        #Total: O(n log(sum(weights)-max(weights)))

        #We dig out the monotonicity of this problem: if we can successfully ship all packages within D days with capacity m, then we can definitely ship them all with any capacity larger than m.
        #Also, answer can only lie between max(weights), sum(weights) which is a
        #sorted array-hence binary search 
        #Now we can design a condition function, let's call it feasible, given an input capacity, it returns whether it's possible to ship all packages within D days. 
        #Then design the boundary, max(weights) to sum(weights) captures all possible
        #capacity values. Now we use condition and the bin search template to find 
        #the MINIMAL capacity that satisfies condition 

        #Binary search template part does the MINIMAL part for you
        #Condition does the true? part for you 

        #Condition should exhibit monotonic behavior, condition(k) is true then 
        #condition(k+1) should also be true 
        #Seek a search space that is sorted, many times it is the given sorted array
        #other times like this, define it yourself 
        

        #The issue many people have when it comes to understanding how a problem like this can be approached using binary search comes down to the way most people learn binary search at first. The traditional implementation of binary search which is shown to most first-time learners gives the impression that the array in question must be sorted, however, the reality is that binary search only cares about a "sorted" search space. Most people assume that the search space of the binary search algorithm has to be the specific elements at a given index in the given array, because those are the examples people tend to be shown when learning binary search. In more advanced binary search problems such as this one, the real trick is figuring out two things: the search space and the condition.