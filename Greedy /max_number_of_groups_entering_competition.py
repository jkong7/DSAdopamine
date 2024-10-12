class Solution(object):
    def maximumGroups(self, grades):
        """
        :type grades: List[int]
        :rtype: int
        """
        #Greedy sort 
        #Maximize number of groups so want each group to only have one more than the 
        #last, 1, 2, 3... pattern 

        #Just sort and then do as many 1/2/3... partitions as possible. This will 
        #ALWAYS work as long as there are numbers available because its in ascending 
        #order. Going left to right, we minimize the working sum for the next partition 
        #So thus the only constraint is the size. As long as there is enough size, 
        #the numbers will always work out

        #Thats the insight that therefore 1/2/3... partitions will ALWAYS work because
        #the sorted order will always work. In the actual soln then, we just count how
        #many of those partitions we can make and that depends PURELY on the length

        n=len(grades)
        part=0 
        incrementer=1
        i=0 
        while i<n: 
            part+=1 
            incrementer+=1
            i+=incrementer
        return part 
