class Solution(object):
    def repeatLimitedString(self, s, repeatLimit):
        """
        :type s: str
        :type repeatLimit: int
        :rtype: str
        """
        from collections import Counter 
        import heapq 

        heap=[]
        ht=Counter(s)
        for char in ht:  
            heapq.heappush(heap, -ord(char))
        
        result=[]
        prev=0 
        streak=0 
        while heap: 
            popped=-heapq.heappop(heap)
            if prev==0 and streak==0: 
                result.append(chr(popped))
                prev=popped
                streak=1 
                ht[chr(popped)]-=1 
                if ht[chr(popped)]!=0: 
                    heapq.heappush(heap, -popped)
                continue 
            if popped==prev: 
                streak+=1 
                if streak>repeatLimit: 
                    streak=1 
                    if heap: 
                        nextt=-heapq.heappop(heap)
                        prev=nextt
                        result.append(chr(nextt))
                        ht[chr(nextt)]-=1 
                        if ht[chr(nextt)]!=0: 
                            heapq.heappush(heap, -nextt)
                    else: 
                        break
                    heapq.heappush(heap, -popped)
                else: 
                    ht[chr(popped)]-=1 
                    result.append(chr(popped))
                    if ht[chr(popped)]!=0: 
                        heapq.heappush(heap, -popped)
            else: 
                streak=1 
                prev=popped 
                ht[chr(popped)]-=1 
                result.append(chr(popped))
                if ht[chr(popped)]!=0: 
                    heapq.heappush(heap, -popped)
        return ''.join(result)

        #Used a heap and a counter hashtable and used pushing popping streak 
        #behaavior, code is pretty messy but it works! heap contains only one of each
        #char and just allows for peaking both current largest AND next largest in 
        #the case where streak>repeatLimit, the freq ht keeps track of counts and 
        #whether or not to push char back in heap 