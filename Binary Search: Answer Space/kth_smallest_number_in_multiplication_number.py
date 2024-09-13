class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        #BS can be used to solve kth smallest... problems!!
        #Monotonicity and condition function: Return true if number has k or more 
        #numbers less than or = to it. Then obviously any number larger than it will
        #also have k or more numbers smaller than it. The MINIMUM number that 
        #passes the condition is the kth smallest number (there could be multiple
        #in the chart). 
        #Search space: Sorted order, 1 to m times n

        #m height 
        #n length 
        #How many numbers in the m x n chart are less than or equal to targetnumber?
        def condition(targetnumber): 
            #find the m and n for target number, mxn is lesscount
            lesscount=0 
            for row in range(1, m+1): 
                lesscount+=min(targetnumber//row, n) #Each row, floor of #/row or n
            return lesscount>=k #O(n)

        left, right=1, m*n #O(mn)
        while left<right: 
            mid=left+(right-left)//2
            if condition(mid): 
                right=mid
            else: 
                left=mid+1 
        return left 

        #The BS will find the MINIMUM number that passes the condition, ie smallest
        #number within the mult table range that has k or more numbers less than or 
        #equal to it. This will return the kth smallest number 
        #O(n log(mn))