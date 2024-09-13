# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: #head.next (one node) check actually not necessary
            return head #either return none or just singular node, respectively
                        #captures both edge cases where rotation isn't necessary

        #get length of LL and start and end
        ogfront=head 
        length=0 
        current=head 
        while current: 
            length+=1 
            end=current 
            current=current.next
            
        #k is periodic so put k into meangingful range 
        k=k%(length)
        if k==0:          #if no rotations just return original list 
            return head 

        #Get to node whose next needs to be set to None (chopped off) and also get
        #the one node after that (will be return node)
        slow=head
        for _ in range(length-k-1):   
            slow=slow.next
        start=slow.next
        #two operations: conenct end to front, chop of next of kth node from end 
        end.next=ogfront
        slow.next=None
        
        return start 

				#O(n) time O(1) space

        #Spent a long time trying to make the slow fast pointer work to get slow
        #where it needed to be. I just needed the check while fast.next and my code
        #with for _ in range(k) to move fast would work (while fast.next for second
        #part to move slow and fast together). 
        #But I realized that I alredy have the length so I can just move one pointer
        #to where it needed to be using length and k. 
        #Handled edge cases (no and 1 nodes), put k into meaningful [0, n-1] range,
        #main chunk is attaching original end to original start, chopping off next
        #pointer at slow, and then returning slow.next which is the new start 
        #Quite a lot of ordering, logic/edge case checks, got it all precisely 


