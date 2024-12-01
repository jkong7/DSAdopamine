class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #n is 10^5, brute force is obviously O(n^2), need some sort of precomputation
        #to cut down to O(n) 
        # [4 3 2 6] [6 4 3 2]

        # 25 -----> 16 -----> 23 -----> 26 
        #   a+b+c-3d  a+b+d-3c  a+c+d-3b

        # Mathematical stepping result I found after experimenting^
        # So O(n) initial computation of F(0), then O(n) prefix sum precomputation 
        # so that each k->k+1 step is only O(1) for a total of O(1) 

        n=len(nums)
        prefix=sum(nums) #O(n)
        initial_sum=sum(i*nums[i] for i in range(n)) #O(n)
        cur_sum, maxx=initial_sum, initial_sum

        for i in range(1, len(nums)): #O(n)
            cur_sum=cur_sum+prefix-(n*nums[-i])
            maxx=max(maxx, cur_sum)
        return maxx 

        #The pattern is a+b+c+d-4d for example, its prefix-(n*nums[-i])
        #took quite a lot of experimenting to find that stepping result 


        