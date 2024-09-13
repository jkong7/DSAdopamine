class Solution(object):
    def maxNumOfMarkedIndices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Yeah to maximize, the greedy intuition is to split into two arrays and then try
        #to pair a num1 with a num2 as many times as possible using BS to minimize the 
        #num2 number

        nums.sort()
        n=len(nums) 
        mid=n//2 
        if n%2==0: 
            nums1=nums[:mid]
            nums2=nums[mid:]
        else: 
            nums1=nums[:mid]
            nums2=nums[mid+1:]

        def BS(num1, nums2, index): 
            def condition(mid): 
                return nums2[mid]>=num1*2 
            left,right=index+1, len(nums2)-1
            while left<right: 
                mid=left+(right-left)//2
                if condition(mid): 
                    right=mid 
                else: 
                    left=mid+1 
            return left if condition(left) else -1 
        
        delete=0 
        index=-1 
        for num in nums1: 
            if index+1<len(nums2): 
                index=BS(num, nums2, index)
                if index!=-1: 
                    delete+=2 
                else: 
                    return delete
        return delete


        #The BEST method is to just do exactly what you did above but just with two 
        #pointers, just left=0 and right starts at mid/mid+1 and do that
        #same logic, this is the most efficient method: 
        nums.sort()
        n=len(nums) 
        mid=n//2 
        left=0 
        if n%2==0: 
            right=mid 
        else: 
            right=mid+1 
        marked=0 
        while right<n: 
            if nums[right]>=nums[left]*2: 
                marked+=2 
                left+=1 
                right+=1 
            else: 
                right+=1 
        return marked 