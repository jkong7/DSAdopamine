class Solution(object):
    def maxSumMinProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nextless=[-1]*len(nums)
        prevless=[-1]*len(nums)
        stack=[]
        for i in range(len(nums)): 
            while stack and nums[stack[-1]]>nums[i]: 
                index=stack.pop()
                nextless[index]=i 
            stack.append(i)
        stack=[]
        for i in range(len(nums)): 
            while stack and nums[stack[-1]]>=nums[i]: 
                stack.pop()
            if stack: 
                prevless[i]=stack[-1]
            stack.append(i)
        
        prefix=[0]*(len(nums)+1)
        for i in range(1,len(nums)+1): 
            prefix[i]=nums[i-1]+prefix[i-1]

        maxx=0 
        for i in range(len(nums)): 
            left=prefix[prevless[i]+1] if prevless[i]!=-1 else 0 
            right=prefix[nextless[i]] if nextless[i]!=-1 else prefix[-1]
            maxx=max(maxx, (right-left)*nums[i])
        return maxx%(10**9 + 7)

        #BOOM, yep mono stack for nextless and prevless and then O(1) prefix sum
        #by finding left and right, each index at nums, we compute the subarray 
        #computation where THAT INDEX is the MINIMUM number (SAME ALLOWED) so 
        #nextless and prevless are STRICTLY less, NOT cutting off same, that was 
        #the difference in my solution at the end that got it. 

        #We basically go as far left and right possible for the subarray at an index
        #i, we go until nums[i] ISNT the min element and cut off right there and then
        #take the prefix sum *min which is prefix sum * nums[i]

        #Mono stack + prefix sum 

        #Hard problem 