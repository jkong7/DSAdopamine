class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """


        k%=len(nums)

        start, end=0, len(nums)-1 
        while start<end: 
            nums[start], nums[end]=nums[end], nums[start]
            start+=1
            end-=1 

        start, end=0, k-1 
        while start<end: 
            nums[start], nums[end]=nums[end], nums[start]
            start+=1
            end-=1 

        start, end=k, len(nums)-1 
        while start<end: 
            nums[start], nums[end]=nums[end], nums[start]
            start+=1
            end-=

#or: 
        n = len(nums)
        k %= n  # This handles cases where k >= len(nums)

        # Reverse the entire array
        nums.reverse()

        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])

        # Reverse the elements from k to the end
        nums[k:] = reversed(nums[k:])

        #In place O(1) extra space method. 
        #First reverse the entire array (O(n) in place) 
        #and then reverse two sections cutoff at k. k must be within the bounds 
        #of len(nums) and if its not just gets its mod equivalent first. 
        #O(n) time O(1) space



        n = len(nums)
        k %= n  # In case k is greater than n

        nums[:] = nums[-k:] + nums[:-k]
        return nums

        #nums[-k:] selects the last k elements of the array.
        #nums[:-k] selects all elements of the array except the last k elements.

        #O(n) time O(n) space. Concatenation creates new arrays which is extra space


        #My first thought, hash table 
        #Go through, match the index to the value 
        numdict={}
        for i in range(len(nums)): 
            numdict[i]=nums[i]
        for i in range(len(nums)): 
            nums[(i+k)%len(nums)]=numdict[i]
        return nums 
        #Got this first try 
        #O(n) time O(n) space 
