class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        boxes=[int(boxes[i]) for i in range(len(boxes))]
        suffix, prefix=0,0
        follow, pre = 0,0 
        for i in range(len(boxes)): 
            if boxes[i]==1: 
                suffix+=i 
                follow+=1 
        result=[0]*len(boxes)
        for i in range(len(boxes)): 
            if boxes[i]==1: 
                follow-=1 
                pre+=1 
                suffix-=i
                prefix+=i
            result[i]=suffix-(follow*i)+(i*pre)-prefix
        return result 

        # O(n^2) obvious with brute force, O(n) with prefix and suffix sums, keep track of 1s that have passed and ones that 
        #are still to come with prefix suffix logic and then use expression to O(1) calculate at each index 
            


 