class StockSpanner(object):
    #How many previous consecutive are less than or equal, monotonic decreasing 

    def __init__(self):
        self.stack=[]
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span=1 #Stands for the fact that span includes itself (new price)
        while self.stack and price>=self.stack[-1][0]: 
            span+=self.stack[-1][1]#New span includes the span of top of stack since
            #new price>=top of stack price 
            self.stack.pop()
        self.stack.append((price, span)) #Keep that span in the stack, a future price
        #>=to this will inherit its span
        return span 


    #
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


#Also solved on the side: Given an array already, return result array
#that represents the number of previous consecutive elements are less
#than or equal to that number (including number itself). Same pattern
#as above using a mono decreasing and popping when >= top of stack:
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        #I think that inside the while loop for popping, you just keep an incrementer

        stack=[]
        result=[1]*len(temperatures)
        for i in range(len(temperatures)): 
            while stack and temperatures[i]>=stack[-1][0]: 
                result[i]+=stack[-1][1]
                stack.pop()
            stack.append((temperatures[i], result[i]))
        return result 
