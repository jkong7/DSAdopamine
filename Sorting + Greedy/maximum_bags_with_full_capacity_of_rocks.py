class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        """
        :type capacity: List[int]
        :type rocks: List[int]
        :type additionalRocks: int
        :rtype: int
        """
        from collections import defaultdict
        from collections import OrderedDict
        ht=defaultdict(int)

        count=0 
        for i in range(len(capacity)): 
            diff=capacity[i]-rocks[i]
            if diff>0: 
                ht[diff]+=1 
            else: 
                count+=1 
        sorted_dict = OrderedDict(sorted(ht.items()))
        for diff in sorted_dict: 
            for _ in range(sorted_dict[diff]): 
                additionalRocks-=diff
                if additionalRocks>=0: 
                    count+=1 
                else: 
                    return count 
        return count 
        #But yeah this is greedy, get the diffs and their freqs, sort the diffs in 
        #ascending order and then subtract of additionalRocks starting from the smallest
        #diffs to make the highest number of completed bags. 
