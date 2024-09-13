class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        memo={}
        def backtrack(start): 
            if start==len(s): 
                return True 
            if start in memo: 
                return memo[start]
            for word in wordDict: #At every level of recursion, explore every single word in wordDict. Use s[start:].startwith to determine if a segment of s matches a 
            #word in wordDict, if so continue down and move start to right after 
            #the addition of that new word, if start can reach the end, its valid 
                if s[start:].startswith(word): 
                    newstart=start+len(word)
                    if backtrack(newstart): 
                        memo[start]=True
                        return True
            memo[start]=False 
            return False 
        return backtrack(0)

        #Backtracking + memoization (just backtracking with the recurrence relation
        #gets TLE, memoization adds necessary efficiency)

#Memoization template: 

#1. Check Memo: if start in memo: return memo[start]
#2. Store Results: memo[start] = result before each return statement.
#This template helps in efficiently solving recursion problems by avoiding redundant #computations.


# Use the 3-liner memoization template when the problem involves overlapping subproblems,
# backtracking or recursion, and state dependence, meaning each state (like an index in a string
# or a position in a grid) has an independent result that can be cached.

# Key indicators include recomputation of the same tasks, subproblem independence,
# and inefficiency without caching, often leading to exponential time complexity.

# Examples include string segmentation, dynamic programming, and grid-based pathfinding problems.

# For `wordBreak`, memoization is effective because the results of `startswith` for each starting
# index in the string are unique and won't change once computed.
