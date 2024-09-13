class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        #make prevless and nextless arrays that hold INDICES, -1 if no 
        prevless=[-1]*len(heights)
        nextless=[-1]*len(heights)

        stack=[]
        for i in range(len(heights)): 
            while stack and heights[i]<heights[stack[-1]]: 
                index=stack.pop()
                nextless[index]=i
            stack.append(i)

        stack=[]
        for i in range(len(heights)): 
            while stack and heights[i]<=heights[stack[-1]]: 
                stack.pop()
            if stack: 
                prevless[i]=stack[-1]
            stack.append(i)
        

        maxarea=0 
        current=0 
        for i in range(len(heights)): 
            if prevless[i]==-1 and nextless[i]==-1: 
                current=heights[i]*len(heights)
            elif prevless[i]==-1: 
                current=nextless[i]*heights[i]
            elif nextless[i]==-1: 
                current=(len(heights)-prevless[i]-1)*heights[i]
            else: 
                current=(nextless[i]-prevless[i]-1)*heights[i]
            maxarea=max(maxarea, current)
        return maxarea 


        prevless = [-1] * len(heights)
        nextless = [-1] * len(heights)

        #nextless is strictly less, prevless is less than or equal 
        stack = []
        for i in range(len(heights)):
            # Process nextless while processing prevless
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                nextless[index] = i
            if stack:
                prevless[i] = stack[-1]
            stack.append(i)

        maxarea=0 
        current=0 
        for i in range(len(heights)): 
            if prevless[i]==-1 and nextless[i]==-1: 
                current=heights[i]*len(heights)
            elif prevless[i]==-1: 
                current=nextless[i]*heights[i]
            elif nextless[i]==-1: 
                current=(len(heights)-prevless[i]-1)*heights[i]
            else: 
                current=(nextless[i]-prevless[i]-1)*heights[i]
            maxarea=max(maxarea, current)
        return maxarea 