class Solution(object):
    def maximumLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        # 1 1 2 1 3 3
        # 1 1 1 2 3 3
        # 1 2 1 2 3 4

        #dp[4][(1+4)%3=2]=dp[1][2]+1
        #dp[4][(1+3)%3=1]=dp[3][1]+1

        #dp[5][(4+1)%3=2]=dp[0][2]+1
        #dp[5][(4+1)%3=2]=dp[4][2]+1


        #alright yeah just ran through the entire example 2 with dp table, 
        #this should be correct: 

        #subproblem: dp[j][i] is max length subsequence ending at index i with all 
        #adjacent pairs of elems mod k is j, j runs from [0, k-1] inclusive 

        #base case(s): Initialize all values of dp table to 1, represents length 1

        #recursion: dp[j][i]=max(dp[j][i]+1) for all z where 
        #z<i and nums[i]+nums[z]%k==j 

        #explanation: At nums[i], look at all previous indices and do the nums[i]
        # + nums[z]%k=j value. The subsequence with pairwise %k=j ENDING at z can 
        #therefore be extended by 1 with nums[i]. 

        #Running time: O(n^2) where n=len(nums). Space: O(nk) 

        #Final result: running max variable update through building up dp cells 

        #Recovering the final result: Prev table with the same k * n dimensions as 
        #dp. At each z<i, if the max dp[j][i] is found here, update prev[j][i] to 
        #be (z,j). Also maintain one (tuple/pair variable) or two variables holding
        #the j, i corresponding with the rolling max variable. After the dp loop, 
        #start at prev[j][i] with the held index values then at each step, note that
        #the nums[i] value and then go to the prev held z,j. Stop after prev[j][i]
        #is the terminal value -1 (initialize prev with all -1s). 

        #Handling case of no optimal solution: input is guaranteed where n>=2
        #the return max variable will always return a result >=2 as any length 2 
        #subsequence is valid. There will always exist an optimal solution therefore

        lastj, lasti=-1,-1
        maxx=1
        n=len(nums)
        dp=[[1]*n for _ in range(k)]
        prev=[[(-1,-1)]*n for _ in range(k)]
        for i in range(1, n): 
            for z in range(i): 
                j=(nums[i]+nums[z])%k
                last=dp[j][z]
                if last+1>dp[j][i]: 
                    dp[j][i]=last+1 
                    maxx=max(maxx, last+1)
                    prev[j][i]=(j,z)
                    lastj, lasti=j,i

        path=[]
        while True: 
            path.append(nums[lasti])
            lastj, lasti=prev[lastj][lasti] 
            if lastj==-1: 
                break

        path.reverse()
        print(path)
        return maxx 

        #!!, got with the path recovery too! 


            