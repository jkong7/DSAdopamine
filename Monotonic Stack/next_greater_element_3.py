class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        #If the number has only decreasing digits ie 4321, then theres no such int, -1 

        #Increasing digits is obv when there is something, lets examine case where both: 
        #14532, okay well 54321, ohhhhh its next greater element with those digits 
        
        #One switch is all it takes to make it the next greater, so I think its you 
        #swith as early as possible and then all the other digits you try to configure
        #as small as possible 

        #Ex: 72543 -> 73245, the swtich happens with 3 taking 2s place and then the 
        #rest of the numbers are just configured in increasing order/smallest 

        #Same tthing with 14532 -> 15234

        #Okay with 560-the switch happens with the first digit, so then it becomes 
        #605 (the 0 and 5 are configured in increasing order)

        #OHHH, and I think the swtich happens with the first digit that has a next 
        #greater element, okay okay nvm I think its the LAST digit that has a next 
        #greater, I mean yeah that makes its SMALLEST greater 

        #Okay yep its exactly that, okay so the final algo should be: 

        #Find the last digit with a next greater, switch that digit with its next greater
        #everything to the left of that digit stays exactly the same and everything to 
        #the right of the digit is compiled in increasing order (minimal)


        stack=[]
        string=str(n)
        nextgreater=[-1]*len(string)

        for i in range(len(string)): 
            while stack and int(string[i])>int(string[stack[-1]]): 
                index=stack.pop()
                nextgreater[index]=i
            stack.append(i)

        lastindex=-1
        for i in range(len(nextgreater)): 
            if nextgreater[i]!=-1: 
                lastindex=i
        if lastindex==-1:
            return -1 

        minn=float('inf')
        switchnum=int(string[lastindex])
        for i in range(lastindex, len(nextgreater)): 
            if int(string[i])>switchnum: 
                minn=min(minn, int(string[i]))

        result=[]
        
        for i in range(len(string)): 
            if i<lastindex: 
                result.append(string[i])
            elif i==lastindex: 
                result.append(str(minn))

        tosort=[]
        flag=False 
        for i in range(lastindex+1,len(string)): 
            num=int(string[i])
            if not flag and num==minn: 
                flag=True 
                continue 
            tosort.append(str(num))
        tosort.append(str(int(string[lastindex])))
        tosort.sort()

        final=result+tosort
        return int(''.join(final)) if int(''.join(final))<=2**31-1 else -1 


        # Mono dec stack and then you find 
        #the last digit that has a next greater, find the LEAST greater to the right of
        #that, and then basically you form ansewr by keeping everything in order from
        #the left of lastindex, switching lastindex to the swapped minn, and then 
        #sorting the rest of the array by first not considering one instance of minn 
        #since it was swapped and also putting in the ognum at lastindex spot, then you
        #sort and append that to the rest of the answer. 


