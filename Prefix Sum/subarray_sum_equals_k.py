class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """   
        prefix=0 
        prefix_counts={0:1}
        count=0 

        for num in nums: 
            prefix+=num 
            if prefix-k in prefix_counts: 
                count+=prefix_counts[prefix-k]
            if prefix in prefix_counts: 
                prefix_counts[prefix]+=1
            else: 
                prefix_counts[prefix]=1 
        return count
        #Rolling prefix sum that we store in a hashmap and for each current prefix
        #sum, we are looking for prefix-k in the dict which means a subarray sum of
        #k: 
        #prefix[r]-prefix[l-1]=k 
        #prefix     prefix-k
        #So the count of prefix-k in the dict is what we add to our result
        #If a prefix sum of prefix-k occured at index l and the current prefix sum is
        #at index r, then the subarray from l+1 to r has sum of k. 
        #Init of 0:1 ensures that the prefix sum of 0 is accounted for which detects
        #subarrays starting from index 0 that sum to k
        #O(n) time and O(n) space (HT)

#Prefix Sum Calculation: Keep a running total of the prefix sums.
#Hash Table: Use a hash table to store the frequency of each prefix sum.
#Check for Subarray Sum: For each new prefix sum, check if prefix_sum - k exists in
#the hash table. If it does, it indicates there is a previous subarray whose sum, 
#when subtracted from the current prefix sum, equals k. Thus, a subarry with sum k 
#exists