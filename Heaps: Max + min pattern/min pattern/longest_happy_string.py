class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        #Longest-optimization 
        #At most, so we want to get to the tipping point to make it the longest 

				#Greedy+heap 
				
        #Always use the largest of the three freqs, greedy heap, but then if 
        #you already used one twice, flag it and the next one has to be the next
        #greatest? 
        import heapq
        heap=[]
        if a: 
            heap.append((-a, 'a'))
        if b: 
            heap.append((-b,'b'))
        if c: 
            heap.append((-c,'c'))
        heapq.heapify(heap) #Okay this is a maxheap now of a,b,c

        #We can compare the largest between heap[1] and heap[2] for the next one

        result=[]
        while heap: 
            if len(result)>=2 and result[-2]==heap[0][1] and result[-1]==heap[0][1]: 
                heapog=heapq.heappop(heap)
                ogfreq, ogletter=heapog
                if heap: 
                    heaper=heapq.heappop(heap)
                    freq,letter=heaper 
                    result.append(letter)
                    if freq+1<0: 
                        heapq.heappush(heap, (freq+1, letter))
                    heapq.heappush(heap, (ogfreq, ogletter))
                else: 
                    return ''.join(result) #Besides the twice used, no other options so can't keep going forward, longest possible happy string 
            else: 
                heaper=heapq.heappop(heap)
                freq, letter=heaper
                if freq+1<0: 
                    heapq.heappush(heap, (freq+1, letter))
                result.append(letter)
        return ''.join(result)

        #First try close! 29/34, i've got some fat ass code to facilitate the 
        #"if already 2 in, I need the next most logic"
        #Second try 33/34 
        #freq+1<0 bc for example (-1,'a') we appended it to our result and that 
        #means there is only one a left and we USED it so we dont want to add back
        
        #But ogfreq+1<=0 because we never used ogfreq after we just peaked it,
        #so for like (-1,'b') and thats ogfreq, we still wanna add it back. And
        #yup, you don't even need any check for pushing og back on, I made that 
        #change. Never made any change to it so can just add it back in 
        #Holy shit and after I made that change my code is fast asffff, 4ms beats 96%

        #TC: O(n logk) in this k=3 so thats basically minimal, n is total # of 
        #chars to process, each char can be processed up to two times due to 
        #pop and push but this simplifies to nlogk