class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #This is one hundred percent a stack problem, append until you get abc then 
        #pop abc off and in the end if stack empty true else false

        stack=[]
        for char in s: 
            stack.append(char)
            if len(stack)>=3 and stack[-1]=='c' and stack[-2]=='b' and stack[-3]=='a': 
                for _ in range(3):
                    stack.pop()
        return not stack 

        