class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.parray=[-1]*len(nums)
        self.parray[0]=nums[0]
        for i in range(1, len(nums)): 
            self.parray[i]=self.parray[i-1]+nums[i]
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.parray[right] if left==0 else self.parray[right]-self.parray[left-1]

