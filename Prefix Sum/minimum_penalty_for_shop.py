class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        #10^5 size, again think O(n)

        #Minimize the penalty 

        from collections import Counter 
        counter=Counter(customers)

        #It seems like its a partition that splits the string into two parts 

        #Minimize number of Ns on the right 
        #Maximize number of Ys on the left 

        #postfix array for number of Ys AFTER an index 

        #prefix array for number of Ns BEFORE index 

        prefix=[0]*(len(customers)+1)
        postfix=[0]*(len(customers)+1)

        for i in range(1, len(customers)+1): 
            prefix[i]=prefix[i-1]
            if customers[i-1]=="N": 
                prefix[i]+=1 
        for i in range(len(customers)-1, -1, -1): 
            postfix[i]=postfix[i+1]
            if customers[i]=='Y': 
                postfix[i]+=1 
        minn, index=float('inf'), None
        for i in range(len(prefix)): 
            if prefix[i]+postfix[i]<minn: 
                minn=prefix[i]+postfix[i]
                index=i 
        return index

        #At any index, the penalty is the sum of prefix count of ‘N’ and suffix 
        #count of ‘Y’.

        #A shop closed at j is closed at j so a Y there doesn't count, so when 
        #we're doing the prefix sums of Y, can't update a current cell +=1 if 
        #its Y, it must be update CURRENt if the PREV was a Y
        #For postfix we don't do this because closed at j means closed at j so 
        #that cell itself counts 
         