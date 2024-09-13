class Solution(object):
    def canChoose(self, groups, nums):
        """
        :type groups: List[List[int]]
        :type nums: List[int]
        :rtype: bool
        """
        groupsindex, index=0,0
        n=len(nums) 
        while index<n: 
            if nums[index]==groups[groupsindex][0]: 
                if nums[index:index+len(groups[groupsindex])]==groups[groupsindex]: 
                    index+=len(groups[groupsindex])
                    groupsindex+=1 
                    if groupsindex==len(groups): 
                        return True 
                else: 
                    index+=1 
            else: 
                index+=1 
        return False 

