class Solution(object): 
    def factorial(self, n): 
        if n==0 or n==1: 
            return 1 
        result=1 
        while n>1: 
            result*=n 
            n-=1 
        return result 
solution=Solution()
print(solution.factorial(5))