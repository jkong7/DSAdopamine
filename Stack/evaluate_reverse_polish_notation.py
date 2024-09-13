import operator 
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #When you get a number, append to stack, continue 
        #When you get an operator, perform the operator on stack[-2] and stack[-1],
        #then pop those 2 (just pop twice) and then push the value result onto 
        #the stack 
        mapp={
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul, 
        }
        
        stack=[]
        for token in tokens: 
            if token not in ['+', '-', '*', '/']: 
                stack.append(int(token))
                continue 
            num2=stack.pop()
            num1=stack.pop() #stack[-2], needs to go after num2, 
            if token!='/': 
                num=mapp[token](num1, num2)
            else: 
                neg=True if (num1<0 and num2>0) or (num1>0 and num2<0) else False
                num=abs(num1)//abs(num2)
                if neg: 
                    num=-num 
            stack.append(num)
        return stack[0]

        #The algorithm is just stack appending when you see a number and when you 
        #see an operator do stack[-2] operator stack[-1], then pop both of those off
        #and replace/push the resulting operator value. 
        #operator.add(num1, num2) is the syntax for that 

        