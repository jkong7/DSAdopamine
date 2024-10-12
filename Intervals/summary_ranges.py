class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        result=[]
        i=0 
        while i<len(nums): 
            j=i+1 
            path=str(nums[i])
            flag=False
            while j<len(nums) and i<len(nums) and nums[j]==nums[i]+1: 
                flag=True
                j+=1 
                i+=1 
            if flag: 
                result.append(path+"->"+str(nums[i]))
            else: 
                result.append(path)
            i=j 
        return result 
            
            
        #Simple two pointer, intervals?? Basically have to be consecutive numbers 
        #to continue the range.         result=[]
        i=0 
        while i<len(nums): 
            start=nums[i]
            while i+1<len(nums) and nums[i+1]==nums[i]+1: 
                i+=1 
            if nums[i]!=start: 
                result.append(str(start)+'->'+str(nums[i]))
            else: 
                result.append(str(start))
            i+=1 
        return result 