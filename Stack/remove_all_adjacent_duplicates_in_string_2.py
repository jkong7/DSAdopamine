class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        #We repeatedly make k duplicate removals on s until we no longer can. 
        #This is a good sign of stack, continued comparison until valid/no more 
        #popping 

        #Yup, its exactly that, keep on pushing, pop happens when we get a length
        #k repeation, this allows add ons to themself form k lengths 
        
        #Yeah check for k length by utilizing the array stack (so you are not using
        #immutable string type and comparing substrings)

        stack=[]
        for char in s: 
            if stack: 
                if char==stack[-1][0]:
                    stack.append((char, stack[-1][1]+1))
                else: 
                    stack.append((char, 1))
            else: 
                stack.append((char,1))
            if stack[-1][1]==k: 
                for _ in range(k): 
                    stack.pop()
        result=[stack[i][0] for i in range(len(stack))]
        return ''.join(result)


        stack=[]
        for char in s: 
            stack.append(char)
            if len(stack[-k:])==k: 
                if len(set(stack[-k:]))==1: 
                    for _ in range(k): 
                        stack.pop()
        return ''.join(stack)

