# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #Probably very similar solution to the slow fast solution in 
        #max twin pair sum 
        #2x fast 1x slow, reverse using slow while at it 
        #prev.next and slow.next compare 
        #Works to get prev and slow in place for even length LL 
        if not head.next: 
            return True
        prev=None
        slow, fast=head, head
        while fast and fast.next: 
            fast=fast.next.next
            next_node=slow.next
            slow.next=prev
            prev=slow
            slow=next_node 
        if fast: 
            slow=slow.next
        while slow: 
            if prev.val!=slow.val: 
                return False 
            prev=prev.next
            slow=slow.next
        return True 

        #O(n) time O(1) space 
        #I had the right idea from the start. Reverse first half and then use prev
        #and slow to diverge and compare and if all nodes are the same, its a 
        #palindrome. Trickier than max twin sum problem since here, length could be
        #even or odd which tripped me up for a long time. 
        #Determine if even/odd by looking at where fast ends in combination with 
        #while fast and fast.next check 

        #Also note for this combination, where the fast=fast.next.next goes in the 
        #loop is important, should go before reversing stuff (examine odd case)

        #If fast ends up at last node and then loop stops, its not none, this is 
        #odd length case and prev ends where it needs to be but slow needs to be 
        #incremented once more (for odd length, middle node doesn't matter, prev
        #and slow need to be one before/after that)

        #Note: Yes, very similar to max twin pair sum solution, slow fast reversing
        #first half using prev and slow, then using prev and slow to compare 
        #There it was adding prev.val, slow.val and finding max, here its making
        #sure all prev.val==slow.val to check for palindrome or not. 

        #Note: Number of nodes is at least 1 so edge case check if just 
        #if not head.next return True
        #If length is 0 or more it would be check 0 and 1 so if not head or not
        #head.next return True

        #Pointer visualization (prev and slow) for even and odd lengths: 

            #p  s
        # 1<-2  3->4

           #p #s #s.n
        #1<-2  3->4->5
  