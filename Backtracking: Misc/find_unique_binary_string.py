class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """

        newnums=[list(num) for num in nums]

        def backtrack(path, start): 
            if start==len(nums): 
                output.append(path)
                return  
            if newnums[start][start]=='1': 
                newpath=path+['0']
            else: 
                newpath=path+['1']
            backtrack(newpath, start+1)
        output=[]
        backtrack([], 0)
        return ''.join(output[0])
        #Okay got it, thats the optimization^^
        #Since there are n strings each of length n, if our answer can just differ 
        #from each string by one digit, we are good. To do this, we just differ the
        #digit at each number. 111, 011, 001, we pick 0 for 1st, 0 for 2nd, and 0
        #for 3rd, basically differ from newnums[nums][nums]. So this targets 
        #one unique bin string 



        #There are 2^n binary string for each n 
        #2^n - n correct answers then 
        newnums=[num.split('') for num in nums]

        def backtrack(path): 
            if len(path)==len(nums): 
                if path not in nums: 
                    output.append(path)
                return 
            for i in range(0,2): 
                newpath=path+str(i)
                backtrack(newpath)
        output=[]
        backtrack('')
        return output[0]

            
        