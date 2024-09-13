class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(path, summ, start): 
            if summ==target: 
                output.append(path)
                return 
            if summ>target: 
                return 
            for i in range(start, len(candidates)): #0-3
                newpath=path+[candidates[i]]
                newsumm=summ+candidates[i]
                backtrack(newpath, newsumm, i)
        output=[]
        backtrack([], 0, 0)
        return output
        #Did it over fast for clarity, filter is the new start is i (not i+1)
        #since same number can be chosen. Use template pattern newpath and newsumm
        #(treat as immutable, I love working with this instead of explicit back
        #track handling with pop). I like to think like oh imma stay the same and
        #ill wait here till you guys are done, ill start you guys off with me 
        #plus something else and go do your thing. 

