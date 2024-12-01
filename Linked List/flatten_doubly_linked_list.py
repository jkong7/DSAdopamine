"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head: 
            return 

        def tail(head): 
            current=head 
            while current: 
                nnode=current.next 
                if current.child: 
                    child=current.child 
                    current.next=child 
                    child.prev=current 
                    t=tail(child)
                    current.child=None
                    if nnode: 
                        t.next=nnode 
                        nnode.prev=t 
                    last=t 
                else: 
                    last=current
                current=nnode 
            return last

        current=head
        tail(current)
        current=head 
        return head 
        #That took a looong time, took the longest time at the end dealing with the 
        #case where there is no next node but there is a child node. tail function 
        #always has to return the last node of the flattened list it processes, 
        #which is either the current node itself or the tail of a child node if it 
        #exists, was just stuck on that case

        #Main idea: Needs to be a recursive function that
        #returns the tail of the current list. Relinking needs to occur at current
        #and child AND between tail of the child to nnode. And then two cases
        #of what tail node can be needs to be handled, pretty challenging 

        #if there is nnode, then we do linking with tail and nnode, otherwise there 
        #is simply no work to do. But last/tail node was neglected at first as the
        #node at the CURRENT level (but there is still a child node below). The key
        #is that last is last at current level IF NO child node otherwise the child
        #node 