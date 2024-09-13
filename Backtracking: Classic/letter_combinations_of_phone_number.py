class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #All possible combinations, 2^n/3^n type problem, no optimization->backtrack
        #problem
        #Another obvious hint is when the lengths are low so that the exponents 
        #cannot get super high to cause overflow 
        if not digits: 
            return []

        ht={
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'], 
            '4': ['g','h','i'], 
            '5': ['j','k','l'], 
            '6': ['m','n','o'], 
            '7': ['p', 'q', 'r', 's'], 
            '8': ['t', 'u', 'v'], 
            '9': ['w', 'x', 'y', 'z'], 
            }
        
        def backtrack(path, start): 
            if len(path)==len(digits): 
                output.append(path)
                return 
            for i in range(start, len(digits)): #234 0-1
                for j in range(len(ht[digits[i]])): 
                    newpath=path+ht[digits[i]][j]
                    backtrack(newpath, i+1)
        output=[]
        backtrack('', 0)
        return output

        #Got it, only thing that was trippin it up was the int and str stuff
        #I had the keys as ints though it should be strs 
        #Outer for loop is just with the start index ands tells you what index
        #of the digits input you are on and the second for loop is just to access
        #the 3-4 letters in each key. Same newpath logic (but with second for loop)
        #to be able to append all 3-4 letters, you then do the same with the next
        #digits index i+1
        