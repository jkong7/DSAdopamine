class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Greedy sort and deal with the ends to minimize diff between largest and smallest
        #Okay so its three moves so always bring up the left and bring down the right 
        #Then for the third move, compare the diff between second to last and third
        #to last with diff between second and third, whichever one is larger is the
        #one you change
        #If len is less than or equal to 4, will always be made 0 
        #Yeah above is not the generalization, you have three moves, in each move, you 
        #compare the difference in the ends (left and right), and whichever is larger 
        #diff is the one you change to adjacent 

        #And yeah this question is more complicated than i thought
        #HMMMM maybe you compared left and right with the MIDDLE 
        #Yep that seems to work 

        #First attempt: 
        if len(nums)<=4: 
            return 0 
        left,right=0,len(nums)-1 
        for _ in range(3): 
            midleft=left+(right-left)//2
            midright=(right+1)//2
            mid=(right+left)//2 + 1
            diff=right-left
            if diff%2==1: 
                if nums[right]-nums[midleft]>nums[midright]-nums[left]: 
                    right-=1
                else: 
                    left+=1 
            else: 
                if nums[right]-nums[mid]>nums[mid]-nums[left]: 
                    right-=1
                else: 
                    left+=1

        return nums[right]-nums[left]


        #-----------------------------------
        if len(nums)<=4: 
            return 0 
        nums.sort()
        return min(nums[-1]-nums[3], nums[-4]-nums[0], nums[-3]-nums[1], nums[-2]-nums[2])



        #Got it at the end, the main insight is that there are only four ways to do it
        #remove 3 from end/start, remove 2 and 1 from end/start, so just find min once
        #those changes are applied. I initially tried to optimize this but ig there is 
        #no way of narrowing it down to 1 so you just have to consider the 4. And since
        #you KNOW through sort+greedy theres only 4 options, you just use those 4, super
        #efficient 

        #Very very similar to min score after changing two elem which I did. Very easy
        #to tell you need to sort and then theres only so much you can do. There, there
        #were 3 options, here theres 4 
