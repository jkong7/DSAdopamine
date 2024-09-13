class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        low, high=0, len(numbers)-1 
        while low<high: 
            if numbers[low]+numbers[high]==target: 
                return [low+1, high+1]
            if numbers[low]+numbers[high]>target: 
                high-=1 
            else: 
                low+=1 

        #O(n) O(1) space (constant extra space)