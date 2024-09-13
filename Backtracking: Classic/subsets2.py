class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(path, start): 
            output.append(path)
            for i in range(start, len(nums)): 
                if i>start and nums[i]==nums[i-1]: 
                    continue 
                newpath=path+[nums[i]]
                backtrack(newpath, i+1)
        nums.sort()
        output=[]
        backtrack([], 0)
        return output

        #Consider 1 2 2 4 5. At the first 2, it will already add everything the 
        #second 2 will add so thats why we skip it. nums[i]==nums[i-1] check 
        #for duplicate works if the list is sorted 
        #Tree 12 12 14 15 for the first wave of backtrack i+1, the 12 cases 
        #will return all duplicates so skip
        #1+(2 2 4 5)
        #2+(2 4 5)
        #skip 2, otherwise duplicate overlap: (2,2)+(4 5)
        #4+(5)
        #(5)
        