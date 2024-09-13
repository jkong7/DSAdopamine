class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        #stack push and pop with ( and ) keep track of indicis in the stack and at the
        #end whatever is remaining in the stack is what we need to remove so just
        #do one for loop and result append anything that is NOT a stack index 
        
        stack=[]
        for i, char in enumerate(s):
            if char=='(': 
                stack.append((i, '('))
            elif char==')': 
                if stack and stack[-1][1]=='(': 
                    stack.pop()
                else: 
                    stack.append((i, ')'))
        remove=set()
        for index,_ in stack: 
            remove.add(index)
        result=[]
        for i,char in enumerate(s): 
            if i in remove: 
                remove.remove(i) 
                continue 
            else: 
                result.append(char) 
        return ''.join(result) 

        #alight but yeah do stack and push pop for VALID parentheses, meaning pop when 
        #you complete a ( with a ). Then whatever is left in the stack is INVALID since 
        #valid leaves the stack empty, so note those invalid indices and then loop 
        #s one more time appending anything that is NOT an invalid index