class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #Permutations cuts down options space by just excluding i 
        #Duplicates so sort and skip duplicates
        def backtrack(path, options):
            if len(path)==len(nums): 
                output.append(path)
                return 
            for i in range(len(options)): 
                if i>0 and options[i]==options[i-1]: 
                    continue
                newpath=path+[options[i]]
                backtrack(newpath, options[:i]+options[i+1:])
            
        nums.sort()
        output=[]
        backtrack([], nums)
        return output

        #i>0, ensures we are not comparing element with a nonexistant previous 
        #element, 
        #1 1 2
        #Skips 1 when its first for loop and i=1 and reduced options is [1,2]
        #Skips 1 when its 2+(1,1) i=1. During i=0, it gets [2,1,1]. During i=1, 
        #it skips 

