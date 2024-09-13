class Solution(object):
    def minimumIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        #At most one dominant element, freq(x)*2>m so yeah the dominant element is 
        #just the most freq one, I think the algo should just be get that freq and 
        #then traverse left to right, noting down freq vs left/right lengths relationshi
        #and the FIRST instance where its that relationship is valid, thats your answer
        #if you find none after traversal then none so return -1 

        from collections import Counter
        counter=Counter(nums)

        maxx=float('-inf')
        dom=-1 
        for val, freq in counter.items(): 
            if freq>maxx: 
                maxx=freq
                dom=val 

        n=len(nums)
        count=0 
        for i in range(len(nums)-1): 
            if nums[i]==dom: 
                count+=1 
                if count/float(i+1)>0.5 and (maxx-count)/float(n-i-1)>0.5: 
                    return i 
        return -1 

        # I was just wrongly considering that the index could go 
        #to the last index when thats not allowed (instructions and the fact that you 
        #will get division by 0). But yeah, very elegant soln, get dom elem + freq,
        #then just maintain prefix count of that elem for the left and you also know 
        #its count on the right using maxx-count. Then you also know the lengths of 
        #left and right through your index so at any i, you can calculate if the 
        #dominant condition holds for both left and right, the first valid is just 
        #the first time this happens. 