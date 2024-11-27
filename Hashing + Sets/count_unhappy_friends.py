class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """
        #Brute force is n/2 * n * n O(n^3) 
        #Lets cut down the n searches through the preference arrays by just doing
        #precomputation - making each preference array a hashtable so you can look
        #up a numbers position in O(1) 
        # n * n precomputation O(n^2) precomputation, 

        # 1: Check position of 0, then for everything to its left, for example 3, 
        # check its pair and compare its position against 1 and if 1 is higher, 
        # unhappy 

        #Need another ht for the friends pairing too

        count=0 
        htfriends={}
        for pair in pairs: 
            htfriends[pair[0]]=pair[1]
            htfriends[pair[1]]=pair[0]

        lookup=[0]*len(preferences)
        for i, array in enumerate(preferences): 
            lookup[i]={array[i]: i for i in range(len(array))}

        for friends in pairs: 
            f1, f2=friends

            f1index=lookup[f2][f1]
            for i in range(f1index): 
                if lookup[preferences[f2][i]][f2] < lookup[preferences[f2][i]][htfriends[preferences[f2][i]]]: 
                    count+=1 
                    break

            f2index=lookup[f1][f2]
            for i in range(f2index): 
                if lookup[preferences[f1][i]][f1] < lookup[preferences[f1][i]][htfriends[preferences[f1][i]]]:
                    count+=1 
                    break 

        return count 