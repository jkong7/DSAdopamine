class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """

        import heapq
        from collections import Counter
        
        # Count the frequency of each word
        wordcount = Counter(words)
        
        # Create a heap where frequency is negated to simulate max-heap behavior
        heap = []
        for key, value in wordcount.items():
            heapq.heappush(heap, (-value, key))
        
        # Extract the k most frequent elements
        result = []
        for _ in range(k):
            value, key = heapq.heappop(heap)
            result.append(key)
        
        return result

        #Got most of it right, even got close to sorting lexicographically using 
        #insert(0, key) insert(1, key) stuff but you need the heap to contain 
        #everything before extracting the k most frequent. Simulating a maxheap 
        #and just appending (adding to right) will take most frequent first and 
        #heap naturally sorts freq ties by selecting the lexicographical lowest
        #(what comes before in the alphabet) so for example, i is selected first 
        #and then love comes after 



        #Build the heap in linear time heapify instad of loop push: 

        # Count the frequency of each word
        wordcount = Counter(words)
        
        # Create a list of tuples with negative frequency to simulate max-heap      behavior
        heap = [(-freq, word) for word, freq in wordcount.items()]
        
        # Convert the list into a heap
        heapq.heapify(heap)
        
        # Extract the k most frequent elements
        result = []
        for _ in range(k):
            value, key = heapq.heappop(heap)
            result.append(key)
        
        return result


        #nlogk solution is minheap and if len(heap)>k, pop. But there's extra 
        #confusing stuff sorting the lexicographical, but idea reamins same, heap
        #size doesn't exceed k
        