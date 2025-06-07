class Solution(object):
    def maximumLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ee, oo, eoeo, oeoe

        even, odd, evenodd, oddeven = -1, -1 ,-1 ,-1
        evenoddlast, oddevenlast = -1, -1

        for num in nums: 
            e = num%2==0 
            firste, firsto=False, False

            if even==-1 and e: 
                even, evenodd = 1, 1
                evenoddlast=0 
                firste=True
            if odd==-1 and not e: 
                odd, oddeven = 1, 1
                oddevenlast=1 
                firsto=True 

            if e: 
                if not firste:
                    even+=1 
                if evenoddlast==1 and not firsto: 
                    evenoddlast=0 
                    evenodd+=1 
                if oddevenlast==1 and not firsto: 
                    oddevenlast=0 
                    oddeven+=1 
            else: 
                if not firsto:
                    odd+=1 
                if evenoddlast==0 and not firste: 
                    evenoddlast=1
                    evenodd+=1 
                if oddevenlast==0 and not firste: 
                    oddevenlast=1 
                    oddeven+=1 
        
        return max(even,odd,evenodd,oddeven)

        #rack eoeo, oeoe, eeee, oooo subsequences 
        #with variables and return max length of those four at the end 
        #O(n) time O(1) space 