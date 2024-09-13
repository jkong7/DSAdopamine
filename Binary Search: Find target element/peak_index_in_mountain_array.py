class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        def condition(targetindex): 
            return arr[targetindex]<=arr[targetindex-1]
        left, right=0, len(arr)-1 
        while left<right: 
            mid=left+(right-left)//2
            if condition(mid): 
                right=mid 
            else: 
                left=mid+1 
        return left-1 

        #Translate the problem to "find the leftmost index in the arr such that
        #the element at the index is less than or equal to the element at the
        #previous index"
        #Left will return one to the right of the actual peak (will be the last
        #element with this condition property, peak is the one larger than it)
        #so return left-1 for peak index