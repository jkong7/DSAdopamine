class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        #Try to do in O(n) 

        #O(n) scan to fill up ht with last index the num occurs at (iterate in rev)
        ht={}
        for i in range(len(arr)-1, -1, -1): 
            if arr[i] not in ht: 
                ht[arr[i]]=i
        
        #For each num, look for if either num//2 or num*2 is in the array and exists
        #somewhere at an index to the right of current index 
        for i, num in enumerate(arr): 
            if (num%2==0 and num//2 in ht and ht[num//2]>i) or ((num*2) in ht and ht[num*2]>i): 
                return True
        return False

        #O(n) time O(n) space hashtable solution 