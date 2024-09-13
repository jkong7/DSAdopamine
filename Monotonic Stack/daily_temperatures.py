class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        #I think that inside the while loop for popping, you just keep an incrementer

        result=[0]*len(temperatures)
        stack=[]
        for i in range(len(temperatures)): 
            while stack and temperatures[i]>temperatures[stack[-1]]: 
                index=stack.pop()
                result[index]=i-index
            stack.append(i)
        return result
