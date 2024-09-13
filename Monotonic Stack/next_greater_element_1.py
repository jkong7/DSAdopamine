from collections import defaultdict
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result=[-1]*len(nums2)

        resultdict=defaultdict(int)
        stack=[] #Pop from right, append to right 
        for i in range(len(nums2)): 
            while stack and nums2[i]>stack[-1]: 
                num=stack.pop()
                resultdict[num]=nums2[i]
            stack.append(nums2[i])
        while stack: 
            num=stack.pop()
            resultdict[num]=-1 
        for i in range(len(nums1)): 
            nums1[i]=resultdict[nums1[i]]
        return nums1

        #Any leftover values in the stack don't have next greater elements so map
        #those values to -1
        #Mono decreasing stack 
     