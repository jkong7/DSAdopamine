class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        #Sort and then one to one map 

        from collections import Counter 
        ht=Counter(changed)
        result=[]
        changed.sort()
        for num in changed: 
            if num in ht and 2*num in ht: 
                result.append(num) 
                ht[num]-=1 
                ht[2*num]-=1 
                if ht[num]==0: 
                    del ht[num]
                if ht[2*num]==0: 
                    del ht[2*num]
        return result if not ht else []

        #if ht becomes empty otherwise false, greedy sort HT 
        #You have to sort because then you may delete wrong x 2x pairs that would have 
        #worked for future nums, iterating x 2x in sorted order ensures this doesn't 
        #happen 
        