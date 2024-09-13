class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #Used only once, so start index should be i+1 to not include i again 
        #No duplicate combinations so sort and skip duplicates  

        def backtrack(path, start, summ): 
            if summ==target: 
                output.append(path)
                return 
            if summ>target: 
                return 
            for i in range(start, len(candidates)): 
                if i>start and candidates[i]==candidates[i-1]: 
                    continue 
                newsumm=summ+candidates[i]
                newpath=path+[candidates[i]]
                backtrack(newpath, i+1, newsumm)
        candidates.sort()
        output=[]
        backtrack([], 0, 0)
        return output 
        
        #Got it, two main things: 1. Each number may be used only once unlike 
        #combiantion sum 1, so to handle this, make start i+1 instead of i to 
        #not allow the same number. 2. Numbers are not nec unique so there can 
        #be repeat combinations. Just like in subsets 2, sort the list and then 
        #skip duplicate numbers 

        #Consider 1 1 2 5 6 7 10, The first 1 will consider 1 2 5 and 1 7 and
        #everything 1 + (2,5,6,7,10). When the BIG for loop shifts and becomes 
        #second 1, it will process the same 1+(2,5,6,7,10) which are ALL 
        #duplicates. So we want to skip

        #1+(1 2 5 6 7 10)
        #SKIPS 1
        #2+(5 6 7 10)
        #etc 

        #i>start ensures duplicates are only skipped after the first iteration of 
        #the main for loop at the current recursion level, Ensures the first 
        #occurrence of each element at the current level is included.
        #First occurence: included, subsequent occurences: skipped 

        #Another example: 1 2 2 4 4 5 6 
        #1+(2 2 4 4 5 6)
        #2+(2 4 4 5 6)
        #2 skipped, otherwise would have produced duplicates: 2+(4 4 5 6)
        #4+(4 5 6)
        #4 skipped, otherwise would have produced duplicates: 4+(5 6)
        #5+(6)
        #6

        #1 2 2 2 4 5 
        #1+(2 2 2 4 5)
        #2+(2 2 4 5)
        #skip both 2s
        #4 + (5)
        #5