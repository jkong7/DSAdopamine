class Solution(object):
    def goodDaysToRobBank(self, security, time):
        """
        :type security: List[int]
        :type time: int
        :rtype: List[int]
        """

        #suffix for increasing going backwards 
        #prefix for decreasing going forwards 

        #Keep track of longest increasing right from index 
        #Keep track of longest decrease left from indx 

        #544 445 

        #security[time:len(security)-time]

        prefix=[0]*len(security)
        for i in range(1, len(security)): 
            if security[i]<=security[i-1]: 
                prefix[i]=prefix[i-1]+1 
            else: 
                prefix[i]=0
        suffix=[0]*len(security)
        for i in range(len(security)-2, -1, -1):
            if security[i]<=security[i+1]:
                suffix[i]=suffix[i+1]+1
            else:
                suffix[i]=0 
        result=[]
        for i in range(time, len(security)-time): 
            if prefix[i]>=time and suffix[i]>=time: 
                result.append(i)
        return result 


        #I did search i in time, n-time as index needs time behind and after to be 
        #valid so we can only search here to make sure that condition is good 
