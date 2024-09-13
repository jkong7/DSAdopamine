class Solution(object):
    def colorTheArray(self, n, queries):
        """
        :type n: int
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        #It happens left to right with queries, like each query and then its computation 
        #fills up the output array in order. So you cant do any sorting im pretty sure 

        #I think we just have to fill up the colors array with each query and then 
        #O(1) or maybe logn find out count of adjacent pairs in that colors state? 

        #Maybe have a prev thats the answer to the prev one and on the current one, 
        #do the i-1, i+1 computation and then add it to prev? But i feel like thats only
        #if theres no overlap. Hmm, I think: 

        #1. If theres no overlap, then its just current + prev 

        #2. If there is overlap, then its prev-(diff of og and current), you just need
        #to calculate the current neighbors of the OG number and then calculate the new
        #one and then increment prev by that amount. 

        #And you dont even need two cases, just do prev-(past-current), that will 
        #answer for both of those 

        #For example, if og had adj count of 2 and new has an adj count of 0, then the
        #answer to that query is prev-2.

        #Thats O(1)^, so O(m) for loop through queries and then O(n) space for colors
        #array. Only edge case should be n=1. Lets do it: 

        if n==1: 
            return [0]*len(queries)

        result=[0]*len(queries)
        colors=[0]*n

        def helper_adj_count(index): #O(1)
            count=0 
            if index==0: 
                if colors[index+1]!=0 and colors[index]==colors[index+1]: 
                    count+=1 
            elif index==len(colors)-1: 
                if colors[index-1]!=0 and colors[index]==colors[index-1]: 
                    count+=1 
            else: 
                if colors[index+1]!=0 and colors[index]==colors[index+1]: 
                    count+=1 
                if colors[index-1]!=0 and colors[index]==colors[index-1]: 
                    count+=1 
            return count 

        #This has to start after the first element of queries is put in btw, okay 
        #the color is at least 1 so we can use 0 to differentiate 

        prev=0 
        for i, query in enumerate(queries): 
            past=helper_adj_count(query[0])
            colors[query[0]]=query[1]
            current=helper_adj_count(query[0])
            result[i]=prev-(past-current)
            prev=result[i]
        return result 

        # well first try I got 172/183, failed on an n==1 case so yeah 
        #theres more edge cases i didnt consider yet ig, lmao its not return [0], its
        #return [0]*len(queries) 
  

        #O(len(queries)) TC and O(n) space (adj checker is O(1)!)

