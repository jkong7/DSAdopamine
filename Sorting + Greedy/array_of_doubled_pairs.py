class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        #I think its just that if every num can be mapped to a *2 num then we are good
        # so we can just use a ht, del x and 2x if pops up, and then
        #return true if ht is empty at the end 
        from collections import Counter 
        arr.sort() 
        ht=Counter(arr)
        for num in arr: 
            if num in ht and num*2 in ht: 
                ht[num]-=1 
                ht[2*num]-=1 
                if ht[num]<=0: 
                    del ht[num]
                if ht[2*num]<=0: 
                    del ht[2*num]
        return not ht 