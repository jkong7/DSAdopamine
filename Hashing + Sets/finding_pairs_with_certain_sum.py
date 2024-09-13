class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        from collections import defaultdict 
        self.oneht=defaultdict(int)
        self.twoht=defaultdict(int)
        self.nums2=nums2
        for num in nums1: 
            self.oneht[num]+=1 
        for num in nums2: 
            self.twoht[num]+=1 
        
        

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        change=self.nums2[index]
        new=self.nums2[index]+val
        self.nums2[index]=new 
        self.twoht[change]-=1 
        self.twoht[new]+=1 

        

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        count=0 
        for num1 in self.oneht: 
            count+=self.oneht[num1]*self.twoht[tot-num1]
        return count 

 
        #This is a good follow up to two sum, num1 and we find its diff with tot in 
        #num2, two hash tables 


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)