# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """

        current=list1 
        for _ in range(a-1): 
            current=current.next
        leftmerge=current

        current=list1
        for _ in range(b+1): 
            current=current.next
        rightmerge=current

        current=list2
        while current: 
            list2endmerge=current
            current=current.next
        leftmerge.next=list2
        list2endmerge.next=rightmerge
        return list1

        #You need node before a, node after b, and last node of list2
        #.next node before a to head of list2 and .next last node of list2 to node
        #after b, thats all the mods you need and then return list1
       