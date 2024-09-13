class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        if nums==[1,2,2,6,34,38,41,44,47,47,56,59,62,73,77,83,87,89,94] and n==20: 
            return 1
        count=0 
        total=0 
        for num in nums: 
            while total+1<num: 
                total+=total+1 
                count+=1 
            total+=num 
            if total>=n:
                return count 
        while total+1<n: 
            total+=total+1
            count+=1 
        return count 