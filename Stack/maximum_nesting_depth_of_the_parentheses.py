class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        #We know its a valid parentheses string so we know that any opener will
        #be closed, we don't have to worry about that. The max nesting depth then
        #is just the max length of our stack at any given moment (guaranteed to 
        #be closed, so the max number if the max depth guaranteed)

        #Any other char we don't care about, it'll just continue the loop

        stack=[]
        length=0 
        for char in s: 
            if char=='(': 
                stack.append('(')
                length=max(length, len(stack))
            elif char==')': 
                stack.pop()
        return length 

        count=0 
        length=0 
        for char in s: 
            if char=='(': 
                count+=1 
                length=max(length, count)
            elif char==')': 
                count-=1 
        return length
        