class Solution(object):
    def canMakePaliQueries(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[bool]
        """

        #Pseudo palindromic logic, if there is at most one number with odd freq, then 
        #we are good, substring can be rearranged, so yeah pseudo palindromic 

        memo={}
        result=[]
        for q in queries: 
            left, right, swap=q[0], q[1], q[2]
            if (left,right) in memo: 
                odd=memo[(left,right)]
            else: 
                odd=0 
                count=Counter(s[left:right+1])
                for freq in count.values(): 
                    if freq%2==1: 
                        odd+=1 
                memo[(left,right)]=odd 
            if odd-(2*swap)<=1: 
                result.append(True)
            else: 
                result.append(False)
        return result 

  
