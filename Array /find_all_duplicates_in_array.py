class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #n int in the range [1,n]
        #Mark 
        result=[]

        for i in range(len(nums)): 
            index=abs(nums[i])-1
            if nums[index]<0: 
                result.append(abs(nums[i]))
            else: 
                nums[index]=-nums[index]
        return result 

        #Really cool, you use the array itself as a marker/hash table kind of thing 
        #because the numbers are in the range 1 to n. That means each number maps 
        #to a UNIQUE index in the array so when we find a duplicate we just check
        #that index to see if its already been marked. 
        