import heapq
class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        #Use first k elements in nums1 and first k elements in nums2

        #k pairs, think heap of size k 
        #(n+m)logk solution is what I'm going for 

        #find k smallest of nums1      nlogk
        #find k smallest of nums 2     mlogk

        #nm pairs in total, we only want to consider n+m pairs? 
        heap=[]
        result=[]
        for j in range(min(k, len(nums2))): #will try to put k elements in 
            heapq.heappush(heap, (nums1[0]+nums2[j], 0, j))
        while heap and len(result)<k: #either heap gets empty (not enough pairs) or result gets filled with k so we stop 
            summ, i, j=heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            #process the next smallest after iniitialization pairs: i+1, j
            if i+1<len(nums1): 
                heapq.heappush(heap, (nums1[i+1]+nums2[j], i+1, j))
        return result

        #Yes, once `i + 1` doesn't pass the if check, the heap will eventually 
        #empty itself without adding anything else for future iterations.

#Initial Heap Size: The heap will contain up to k pairs if there are enough 
#elements in nums2.
#Heap Emptying: If the heap empties before reaching k pairs, it means there 
#weren't enough pairs available.

#Next Pairs: The pair (nums1[i+1], nums2[j]) will potentially provide the 
#next smallest sum after the initial pairs.

        

        
        


        #k^2 logk, super inefficient, TLE 
        heap=[]
        for i in nums1[:k]: 
            for j in nums2[:k]: 
                heapq.heappush(heap, (-(i+j), [i,j]))
                if len(heap)>k: 
                    heapq.heappop(heap)
        result=[]
        for summ, pair in heap: 
            result.append(pair)
        return result 
        