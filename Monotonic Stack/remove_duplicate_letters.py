class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Smallest lexicographical order, sounds similar to remove k digits to make 
        #number as small as possible. If we find a next SMALLEST, we remove the 
        #number 
        #Here should be the same thing 

        #How many to remove? Until the string has each unique letter only once 
        #Greedy monotonic remove. Mono inc stack, for example 1 3 5    4
        #Remove the 5 from the stack and keep the 4. 134<135, then if not 
        #up to remove count, then at the end, we remove remaining remove count 
        #elements from the back. This is case of increasing order 13456, removing
        #from the back is the most minimize way. 

        #Yeah so thats how we translate this problem 

        #REMOVING characters from the string, cannopt REORGANIZE, yeah so this 
        #seems identical to remove k digits to minimize 

        #Think about a mono inc, whenever we get a lesser element we want to keep
        #the lesser and discard the greater to minimize, this is what the mono inc
        #invariant does for us 

        #Every letter can only appear once though, shittt

        #Maybe can still greedy it, if a letter is already in the stack, simply skip?

        #Probably have to combine with a freq dict and only pop when condition 

        #You can only pop from the stack if there is still more in the future 
        from collections import Counter 
        freqdict=Counter(s)
        charSet=set()

        stack=[]
        for char in s: 
            freqdict[char]-=1 
            if char in charSet: 
                continue 
            while stack and char<stack[-1] and freqdict[stack[-1]]>0: 
                c=stack.pop()
                charSet.remove(c)
            stack.append(char)
            charSet.add(char)
        return "".join(stack)


        #Got it!! HT, set, and mono stack usage 


#Yes, this problem is similar to "Remove K Digits" in the sense that both involve 
#using a stack to maintain a sequence (either numbers or characters) in a way that
#ensures the smallest possible lexicographical order. Both problems use a greedy
#approach to remove elements that would lead to a larger lexicographical order while
#preserving the required constraints.
