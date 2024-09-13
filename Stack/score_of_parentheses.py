class Solution(object):
    def scoreOfParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        total=0 
        stack=[]
        for char in s: 
            if char=='(': 
                stack.append(char) 
            else: 
                num=0
                if stack[-1]=='(': 
                    stack.pop()
                    stack.append(1) 
                else: 
                    while stack[-1]!='(': 
                        num+=stack.pop()
                    stack.pop()
                    stack.append(2*num)
        return sum(stack) 
        #Yeah so if ( append and then if ), if the next one is just a (, thats a score
        #of 1 which we append to stack after popping off the 1. If the next after ) isnt
        #directly a (, we know its numbers that we appended before. The rule is that we
        #add these scores so we accumualate that sum up until its a ( for which we pop
        #and stop and then append 2*accumulated sum as the ( completes the (A) case
        #for which we have to multiply by 2. At the end its either all merged into one
        #number of adjacent numbers so we return sum of stack. 