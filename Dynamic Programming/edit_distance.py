class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        #subproblem:
        #dp[i][j] represents minimum operations to turn word1[0...i] to word2[0...j]

        #base cases: dp[0][j]=j for all j<=len(word2)
        #            dp[i][0]=i for all i<=len(word1)

        #recurrence plus explanation: 
        #dp[i][j]=min: 
        #         a_i=b_j: dp[i-1][j-1]
        #         replace a_i with b_j to a: dp[i-1][j-1]+1
        #         delete a_i: dp[i-1][j]+1
        #         insert b_j: dp[i][j-1]+1 

        #return: dp[n][m]

        #dp table size: (n+1) by (m+1)
        
        #0 1 2 3
        #1 0 0 0
        #2 0 0 0 
        #3 0 0 0 
        #4 0 0 0 
        #5 0 0 0 

        n,m=len(word1), len(word2)
        dp=[[float('inf')]*(m+1) for _ in range(n+1)]

        for i in range(m+1): 
            dp[0][i]=i
        for i in range(n+1): 
            dp[i][0]=i 

        for i in range(1, n+1): 
            for j in range(1, m+1): 
                if word1[i-1]==word2[j-1]: 
                    dp[i][j]=dp[i-1][j-1]
                dp[i][j]=min(dp[i][j], dp[i-1][j-1]+1,
                             dp[i-1][j]+1, 
                             dp[i][j-1]+1)
        return dp[n][m]
