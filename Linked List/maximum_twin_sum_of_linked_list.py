# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """

        current1, current2=head, head 
        nodecount=0 
        numdict={}
        while current1: 
            nodecount+=1
            current1=current1.next
        iterator=0 
        while current2: 
            if iterator in numdict: 
                numdict[iterator]+=current2.val
            else: 
                numdict[nodecount-1-iterator]=current2.val
            current2=current2.next
            iterator+=1
        return max(numdict.values())


        prev=None 
        slow, fast=head, head 
        twinsum=0 
        while fast and fast.next: 
            fast=fast.next.next
            next_node=slow.next
            slow.next=prev 
            prev=slow 
            slow=next_node
        while slow: 
            if prev.val + slow.val > twinsum: 
                twinsum=prev.val+slow.val
            prev=prev.next
            slow=slow.next
        return twinsum 
        #This is the optimal O(n) one pass no extra space method with two pointers
        #Quite genius. Read about it and then got the implementation first try 
        #Have a slow fast (twice fast) to analyze the first half of the list 
        #While this is going on, reverse the first half using the slow pointer 
        #while fast races to the end (which is when reversing stops). This is just 
        #done with the four liner reverse LL code. Then, recall that prev now points
        #to the start of the reversed LL, slow now points to the start of the second
        #half. 
        #Can still think of the LL as 1->2->3->4 but the pointers in the first half
        #now point left. #Traversing slow.next and prev.next now goes opposite ways 
        #and twin sums will be calculated at each prev.val+slow.val so second while
        #loop calculates/updates these until slow reaches the end. 
        #Note: No need to check if not head or not head.next since # of nodes
        #is 2 or more 

        #         p  s
        #1<-2<-3<-4  5->6->7->8

