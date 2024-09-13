class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #IMPORTANT note for all backtracking: 
        #How to identify? "return a list of all possible", you HAVE to go through 
        #every possibility. When there's no optimization-min/max, shortes/longest
        #etc, its all possibilities so its prob backtracking
        #Also super easy to identify when the constraint lengths are small since 
        #backtracking problems grow super super fast (exponentially with input size)


        def backtrack(path, start): #inputs are path+options space filter 
            output.append(path)
            for i in range(start, len(nums)): 
                newpath=path+[nums[i]]
                backtrack(newpath, i+1)
        output=[]
        backtrack([], 0)
        return output
        #Did it over fast for clarity. No validation (every path is valid), ends
        #when overarching for loop ends 


        def backtrack(path, start): 
            options.append(path[:]) #Any path is valid 
            for i in range(start, len(nums)): 
                path.append(nums[i])
                backtrack(path, i+1) #The new options space consists of elements to the right of nums[i]
                path.pop()
        options=[]
        backtrack([], 0)
        return options
        #O(n*2^n) 2^n subsets and n time to copy/listify tuple for path to output

        #Validation: Any path is valid 
        #Return: for loop ending, naturally unwinds the call stack 
        #Epxloration: to get a new options space, we consider only elements in the 
        #array to the right of current 
        
        
  #available_options = xxx
	#for i in available_options:
	#	node.append(i)
	#	traverse(rval, node, input_data)
	#	node.pop()
