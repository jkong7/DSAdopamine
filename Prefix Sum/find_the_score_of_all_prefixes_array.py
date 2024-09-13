class Solution(object):
    def findPrefixScore(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #so they want a prefix sum array of the conversion array 

        conversion=[-1]*len(nums)
        prefix=[-1]*len(nums)

        maxx=float('-inf')
        for i in range(len(nums)):
            maxx=max(maxx, nums[i])
            conversion[i]=nums[i]+maxx
        prefix[0]=conversion[0]
        for i in range(1, len(nums)):
            prefix[i]=conversion[i]+prefix[i-1]
        return prefix
        