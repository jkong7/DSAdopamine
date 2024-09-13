class Solution(object):
    def minOperations(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """

        nums.sort()
        #[1,3,6,8]

        #[0, 1,4,10,18]
        #[18,17,14,8,0]

        n=len(nums)
        result=[0]*len(queries)
        prefix=[0]*(len(nums)+1)
        for i in range(1, len(nums)+1): 
            prefix[i]=prefix[i-1]+nums[i-1]

        def BS(targetnumber): 
            def condition(mid): 
                return nums[mid]>=targetnumber
            left,right=0,len(nums) 
            while left<right: 
                mid=left+(right-left)//2
                if condition(mid):
                    right=mid
                else: 
                    left=mid+1 
            return left 
        
        summ=sum(nums)
        #suffix[i]-(# of suffix*num) + (num*#of prefix)-prefix[i]) 
        for i,q in enumerate(queries): 
            index=BS(q)
            result[i]=(summ-prefix[index])-((n-index)*q)+(index*q)-prefix[index]
        return result 

        #suffix[i]-((# of suffix)*querynum)+(querynum*(# of prefix)-prefix[i])


        
        