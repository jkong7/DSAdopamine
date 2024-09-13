class Solution(object):
    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #After sorting, go through left to right of the numbers, note down the difference
        #with the number and target and then find index of the first num that is less 
        #than or equal to that diff. Then everything between that index and current 
        #number index is valid which we count using 2^(r-l), (between a width of n, 
        #total num of subsequence is 2^n) and we know everything in our range between
        #l exclusive and r inclusive is valid so that subsequences INCLUDING left num
        #provides 2^(r-l) to count 

        nums.sort() #nlogn
        #For bin search, we can do first num that is greater than or equal to targetnum
        #and then return left if nums[left]==targetnumber else left-1 
        def BS(targetnumber): 
            def condition(mid): #First number less than or equal to targetnumber 
                return nums[mid]>targetnumber 
            left,right=0,len(nums)-1 
            while left<right: 
                mid=left+(right-left)//2
                if condition(mid): 
                    right=mid 
                else: 
                    left=mid+1 
            if targetnumber>=nums[-1]: 
                return len(nums)-1 
            else: 
                return left-1 

        total=0 
        for l in range(len(nums)): #nlogn
            targetnumber=target-nums[l]
            if nums[l]<=targetnumber: 
                r=BS(targetnumber) 
                total+=2**(r-l)
        return total%(10**9+7)
        #The one off error with duplicates made me change the bs condition to strictly
        #greater and not greater than or equal cause equal would choose the leftmost
        #value when we want the rightmost so strictly greater and left-2 will always 
        #return the rightmost 

        #Helpful math summary note that i've already been using: 
        #Total num of subarrays is 1+2+...+n=n(n+1)/2 
        #Total num of subsequences/subsets is nC0+nC1+...+nCn=2^n 