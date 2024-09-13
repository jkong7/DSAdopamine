class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        #Both interval lists are already sorted 

        #Two pointers 
        #i for first list 
        #j for second list 

        #Always move the pointer who has the shorter of the two ends 


        i,j=0,0
        result=[]
        while i<len(firstList) and j<len(secondList): 
            start=max(firstList[i][0], secondList[j][0])
            end=min(firstList[i][1], secondList[j][1])
            if start<=end: #Means that there is an overlap (in any scenario)
                result.append([start, end]) #Will handle every single overlap case,
                #this is why you use max and min for start and end 
            if firstList[i][1]<secondList[j][1]: #Increment the pointer whose interval ends first 
                i+=1 
            else: 
                j+=1 
        return result

        #Did it myself in one go after trying a casework approach 

        #I initially tried a casework approach, I don't know why, when I should 
        #immediately just of thought of using max of start and min of end, this is 
        #standard for interval merge/intersection/overlap problems 
        #But I did get the interval appends right and the logic that you should 
        #always inrement the pointer of the interval who ends first in the pair 