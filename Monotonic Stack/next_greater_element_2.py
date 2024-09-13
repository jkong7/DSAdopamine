class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[-1]*len(nums)
        stack=[]
        twopass=len(nums)*2
        for i in range(twopass): #0 to 5  3
            index=i%len(nums)
            while stack and nums[index]>nums[stack[-1]]: 
                ind=stack.pop()
                result[ind]=nums[index]
            stack.append(index)
        return result 

        #To deal with circular array here, use mods, here we need to traverse the 
        #array exactly twice as an element's next greater element can be on the 
        #wrap around traversal. So you do for i in range(2*len(nums)) and the index
        #you process from the loop is i mod len(nuns)
        #In general, to deal with circular arrays, just use i=i%len(nums)