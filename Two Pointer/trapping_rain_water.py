class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #Two pointer soln: Understood, always pick the lower of left and right
        #since lower height determines boundary, lmax-left current determines 
        #the area gain from one of the heights, no gain from a current height
        #relative to lmax if current height is >= lmax so just update lmax to 
        #that current height 
        
        left,right=0, len(height)-1 
        lmax, rmax=0,0
        area=0
        while left<right: 
            if height[left]<height[right]: 
                if height[left]>=lmax: 
                    lmax=height[left]
                else: 
                    area+=lmax-height[left]
                left+=1 
            else:
                if height[right]>=rmax: 
                    rmax=height[right]
                else: 
                    area+=rmax-height[right]
                right-=1 
        return area

        stack = []
        total_water = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                bottom = stack.pop()
                if not stack:
                    break
                width = i - stack[-1] - 1
                water_height = min(height[i], height[stack[-1]]) - height[bottom]
                total_water += width * water_height
            stack.append(i)
        return total_water














        #For each height find the next greater than or equal to height
        #Until then the area is (index2-index1-1)*height-sum of heights less 
        #than that height in that range (everything in the range because it won't
        #trigger condition)
        #If it has no greater than or equal, it doesn't contribute to area? 


        #Consider the largest index difference between element and next >=
        #then everything in between is subtracted from rectangle width? 

        #Next largest index, index difference (like daily temperatures)

        nextlarge=[-1]*len(height)
        prevlarge=[-1]*len(height)
        stack=[] #Mono decreasing 
        for i in range(len(height)): 
            if height[i]==0: 
                nextlarge[i]=(0,0)
                prevlarge[i]=(0,0)
                continue 
            while stack and height[i]>=height[stack[-1]]: 
                index=stack.pop()
                nextlarge[index]=(i, i-index-1) #3 to 7, 3 in between 
            if stack: 
                prevlarge[i]=(stack[-1], i-stack[-1]-1)
            stack.append(i)


        #Greedy, process distances as they come and cover ground 
        #Try to process nextlarge FIRST if not (0,0)/-1. else if nextlarge is that 
        #BUT nextless isn't, process nextless, otherwise both are that so skip 
        i=0 
        area=0 
        while i<len(height): 
            if nextlarge[i] not in [(0,0), -1]:
                start=height[i]*nextlarge[i][1]
                for j in range(i+1, nextlarge[i][1]+i+1): 
                    start-=height[j] 
                area+=start
                i=nextlarge[i][0]
            elif prevlarge[i] not in [(0,0), -1]: 
                start=height[i]*prevlarge[i][1]
                for j in range(prevlarge[i][0]+1, i): 
                    start-=height[j]
                area+=start
                i+=1 
            else: 
                i+=1 
        return area 

        #^I am getting correct for cases where all the area is calculated with
        #next greater, but theres also cases where an area is calculated even 
        #when a next greater isn't present 
        #Adjacent heights dont catch rain, rep by a dist of 0 in my code so handles
        #that
        #^Okay boom I put in nextless and my greedy algo goes nextlarge first, if 
        #not then nextless, if not both then i+=1. 

        #Welp found out that you need prev large not nextless, consider 4 2 3 
        #So implemented prevlarge instead of nextless, could do it with the same
        #pass/loop as nextlarge, pretty sick, nextlarge is nextlarge or equal and 
        #so prevlarge is strictly larger 
        
        #Nextlarge and prevlarge: 202/322



        