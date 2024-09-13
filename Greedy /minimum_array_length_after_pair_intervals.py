class Solution(object):
    def minLengthAfterRemovals(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Our goal is to maximize nums[i]<nums[j] pairs 
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
                return nums2[mid]>num1
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
                    return n-delete
        return n-delete


        n=len(nums) 
        mid=n//2 
        left=0 
        delete=0 
        if n%2==0: 
            right=mid 
        else: 
            right=mid+1 
        while right<n: 
            if nums[right]>nums[left]: 
                delete+=2 
                right+=1 
                left+=1 
            else: 
                right+=1 
        return n-delete
