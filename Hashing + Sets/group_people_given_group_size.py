class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """

        from collections import defaultdict
        ht=defaultdict(list)
        for i, size in enumerate(groupSizes): 
            ht[size].append(i) 
        result=[]
        for size in ht: 
            rounds=0 
            index=0 
            while rounds<len(ht[size])//size:
                a=[]
                for _ in range(size): 
                    a.append(ht[size][index])
                    index+=1 
                result.append(a)
                rounds+=1 
        return result 

        
        