class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #If you see a number, append [ to stack and then if you see a [, just continu
        #(number guarantees a [ follow so we can handle both at the same time)

        #Once you get a closer, you append number times 

        #If stack closes, empty it and append to result 

        #Insight?? Number stands for muliplication and letter is an add 

        stack=[]
        for char in s: 
            if char!=']': 
                stack.append(char)
                continue 
            #From here, char is guaranteed to be ]
            combinedletters=''
            while stack and stack[-1]!='[': 
                combinedletters=stack.pop()+combinedletters
            stack.pop() #To pop the [
            combinednumber=''
            while stack and stack[-1] in '0123456789': 
                combinednumber=stack.pop()+combinednumber
            stack.append(int(combinednumber)*combinedletters)
        joined=''.join(stack)
        return joined

        #Nice nice, watched the neetcode drawing a bit and then implemented it fully
        #myself flawlessly in one try, the stack vision is again append and pop WHEN you see 
        #a certain thing, thats how all these stack problems are. Here you append
        #everything until you see a ]
