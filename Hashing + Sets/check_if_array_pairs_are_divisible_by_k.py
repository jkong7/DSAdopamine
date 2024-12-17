class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        """
        #Can probably just use two sum logic for this, can group together numbers 
        #based on their modulo with k and then for each num just need to find 
        #its modulo pair 

        from collections import defaultdict 
        ht=defaultdict(int)
        for num in arr: 
            ht[num%k]+=2
        if ht[0] and (ht[0]//2)%2!=0: 
            return False
        n=len(arr)
        count=0 


        for i in range(n): 
            mod, complement = arr[i]%k, 0 if arr[i]%k==0 else k-(arr[i]%k)
            ht[mod]-=1
            if ht[mod]==0: 
                del ht[mod]
            if ht[complement]: 
                ht[complement]-=1 
                count+=1 
                if ht[complement]==0: 
                    del ht[complement]
        return count==n



        #mod in python deals with negatives so no need extra handling, basically it 
        #came down to one extra exterior case which is mod 0 (perfectly divisible 
        #by k numbers), there HAS to be an EVEN number of those. Other mods don't 
        #need to have an even freq for example having 1 num with mod 1 is okay 
        #cause there can be another num with mod 3 for example (k=4) and that works
        #mod 0 takes from its own pool so has to be even for pairs 