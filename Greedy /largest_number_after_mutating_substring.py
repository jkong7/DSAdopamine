class Solution(object):
    def maximumNumber(self, nums, change):
        """
        :type num: str
        :type change: List[int]
        :rtype: str
        """
        result=[]
        i=0 
        n=len(nums) 
        flag=False
        while i<n: 
            if not flag: 
                if change[int(nums[i])]>int(nums[i]):
                    flag=True 
                    while i<n and change[int(nums[i])]>=int(nums[i]):
                        result.append(str(change[int(nums[i])]))
                        i+=1 
                else: 
                    result.append(nums[i])
                    i+=1 
            else: 
                result.append(nums[i])
                i+=1 
        return ''.join(result)
