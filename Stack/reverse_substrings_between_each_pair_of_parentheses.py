class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        #Anytime you see operations with nested paren/brackets, think linear left
        #to right stack, popping when you see a closer and doing something with that

        #Yeah so here, append everything to the stack and the key popper is just
        #the closer paren ), for which you pop UNTIL you get to the opener (, this
        #whole time you create the reversed substring with the poppers by just using
        #reverse concatenation. reverse='', reverse=reverse+stack.pop(), and then
        #do an independent pop for the opener ( and then append back to the stack
        #the reversed string 
        #Can't return the reversed substring appended as one stack entry, need the 
        #individual letters again, so for loop with stack append
        #At the end return ''.join(stack)

        stack=[]
        for char in s: 
            if char!=')': 
                stack.append(char)
                continue 
            #From here, char is guaranteed to be )
            reverse=''
            while stack and stack[-1]!='(': 
                reverse=reverse+stack.pop()
            stack.pop() #To pop the (
            for i in reverse: 
                stack.append(i)
        return ''.join(stack)