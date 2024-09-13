class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """

        stack=[]
        for char in s: 
            if stack and char!=stack[-1] and (char.lower()==stack[-1] or char.upper()==stack[-1]): 
                stack.pop()
            else: 
                stack.append(char)
        return ''.join(stack)

  