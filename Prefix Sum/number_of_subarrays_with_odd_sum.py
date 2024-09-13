class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        n=len(arr)
        prefix=[0]*len(arr) 
        prefix[0]=arr[0]
        odd,even=0,0
        if arr[0]%2==1: 
            odd+=1 
        else: 
            even+=1 
        for i in range(1, len(arr)): 
            prefix[i]=prefix[i-1]+arr[i]
            if prefix[i]%2==1: 
                odd+=1
            else: 
                even+=1 

        total=n*(n+1)//2 
        even_sub=even+(odd*(odd-1))//2 + (even*(even-1))//2
        return (total-even_sub)%(10**9 +7)

        #in counting helps so much with problems like this. First construct the prefix sum 
        #array, we want to count the INVALID subarrays which are those that have even
        #sums. We get an even sum through an even prefix number, two odd numbers, or 
        #two even numbers (since odd-odd and even-even are even). Thus any other subarray
        #will have an odd number so we do total (n(n+1)//2)-even_sub to get num of 
        #odd_sub, complementary counting. The odd odd and even even are just odd choose 2
        #and even choose 2 
