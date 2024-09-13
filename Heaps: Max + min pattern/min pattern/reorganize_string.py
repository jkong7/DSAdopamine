import heapq
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # rrrabbtttt.   r:3 a:1 b:2 t:5
        #rbtrbtrtat
        #Get freqs, always insert the max freq letter EXCEPT the previously inserted
        #letter 

        # aab aba

        #trtrtbtabt     4 2 3 1 2

        #Use maxheap to always store the largest freq character 

        sdict={}
        max_allowed = (len(s) + 1) // 2  # Calculate maximum allowed frequency
        for letter in s: 
            if letter in sdict: 
                sdict[letter]+=1 
            else: 
                sdict[letter]=1 
            if sdict[letter]>max_allowed: 
                return ""
        heap=[]
        for letter, freq in sdict.items(): 
            heapq.heappush(heap, (-freq, letter))


            #r:3 a:1 b:2 t:4
            #First pop t, then only look at r a b 
            #Pop and then put into temp storage with a one decremented freq 

            #Only if len(temp_storage)>1 do we push it back onto the heap
            #(that simulates a wait time of one in between)
            #Ah, we use a first in first out for temp_storage? 
            #like we first add t then r but then we want to put t back out 
            #pop[0] takes from the left and append adds to the right so we 
            #simulate queue behavior 

        #length of heap changes as elements are pushed back (for loop used when you 
        #want k number of pops and the for loop is range k), so here use a while loop
        newstring=''
        temp_storage=[]
        while heap: 
            freq, letter=heapq.heappop(heap)
            newstring+=letter

            if freq<-1: 
                temp_storage.append((freq+1, letter)) #decremented freq

            if temp_storage and letter!=temp_storage[0][1]: 
                heapq.heappush(heap,temp_storage.pop(0))
        #aba example: a b, and then heap empty but temp_storage still holds (1,a)
        #so after loop, still need to use temp storage

        #If freq of element exceeds half rounded up of len s, its not possible in 
        #the first place, I added that edge case check during the freq dict building
        #Just had to make minor logical changes to temp_storage, not len > 1 check, 
        #its current letter doesn't equal the most recently added letter, then push
        #it back 
        #At the end, temp_storage can have more than one element, pop and add letter
        #if the freq is ever more than 1, that means its impossible for no same adj 
        while temp_storage: 
            freq, letter=temp_storage.pop(0)
            if freq<-1: 
                return ""
            else: 
                newstring+=letter
        return newstring 


        #n logk (heap push and pop operations based on number of unique characters k)
        #NUMBER of heap operations is not just k since reinsertion logic makes the 
        #number of heap operations more and can scale to n
