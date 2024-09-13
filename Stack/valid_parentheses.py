class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Stack of one direction, do ( 
        stack=[]
        for i in s: 
            if i in ['(', '{', '[']: 
                stack.append(i)
                continue 
            #From here, its a closing bracket 
            if not stack or stack[-1] + i not in ["()", "{}", "[]"]:
                return False 
            stack.pop()
        return False if stack else True 


        #Trying to empty the stack goes towards valid, if its not empty at the end
        #means not every opening had a close so false. Inside the loop, false if
        #top combined with current doesn't form a close pair OR stack is empty (which
        #means a closer doesn't have an opener). Open brackets get 
        #appended and if have pairs, continue and pop. 