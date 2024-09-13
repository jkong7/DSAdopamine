class Solution(object):
    def prevPermOpt1(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        #Largest lexicographically number that is smaller than arr 
        #This seems very similar to next greater element 3 which was basically smalles
        #number larger than current 

        #So we want to swap the LAST number that has a next smaller and we want to 
        #swap it with the LARGEST number to its right and then sort everything to 
        #the right in increasing order 

        #Yeah okay its lexicographically largset thats smaller. So yeah the FIRST num
        #that has next smaller we swap it with the LARGEST number that is smaller than it
        #and then the remaining elements we sort in increasing order

        #We DONT even have to sort the remaining as they will ALREADY be in that order
        #since we know none of those numbers have a nextless which tells us its already
        #in non dec order 

        #So all we have to do is swap lastindex (nextless last index) with maxswap index
        #(largest num less than lastindex num)


        nextless=[-1]*len(arr)
        stack=[]
        for i in range(len(arr)): 
            while stack and arr[i]<arr[stack[-1]]: 
                index=stack.pop()
                nextless[index]=i 
            stack.append(i)

        lastindex=-1 
        for i in range(len(nextless)): 
            if nextless[i]!=-1: 
                lastindex=i 
        if lastindex==-1: 
            return arr 

        maxswap=0 
        swapindex=-1
        for i in range(lastindex, len(arr)): 
            if arr[i]<arr[lastindex]: 
                if arr[i]!=maxswap: 
                    maxswap=max(maxswap, arr[i])
                    swapindex=i 
        arr[lastindex], arr[swapindex]=arr[swapindex], arr[lastindex]
        return arr

        #Got stopped at edge case [3,1,1,3] where we are supposed to swap 3 with the firs
        #1 not the second. 52/54 


        lastindex=-1 
        minn=arr[-1]
        for i in range(len(arr)-2,-1,-1): 
            if arr[i]>minn: 
                lastindex=i
                break 
            minn=min(minn, arr[i])

        if lastindex==-1: 
            return arr

        maxswap=0 
        swapindex=-1
        for i in range(lastindex, len(arr)): 
            if arr[i]<arr[lastindex]: 
                if arr[i]!=maxswap: 
                    maxswap=max(maxswap, arr[i])
                    swapindex=i 
        arr[lastindex], arr[swapindex]=arr[swapindex], arr[lastindex]
        return arr
        #This finds the first index with a nextless just using a right to left scan
        #(so no stack space), but it still needs to find the largest num smaller than it
        #O(n) and O(1) 

        #17469 is NOT lexicographically larger than 17964 LMAO but its cause one swap 

