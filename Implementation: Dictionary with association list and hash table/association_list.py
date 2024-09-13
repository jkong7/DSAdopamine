struct _node:
    let key 
    let value 
    let next 
    
  
class AssociationList[K, V] (DICT):

    let head

    def __init__(self):
        self.head = None

    # See above.
    def __print__(self, print):
        print("#<object:AssociationList head=%p>", self.head)

    def len(self):
        let count=0
        let current=self.head
        while current is not None: 
            count=count+1
            current=current.next
        return count 
    
    def mem?(self, key): 
        let current=self.head 
        while current is not None: 
            if current.key ==key: 
                return True 
            current=current.next
        return False 
        
    def get(self, key): 
       let current = self.head 
       while current is not None: 
           if current.key==key:
               return current.value 
           current=current.next
       error("key not found in dictionary")
       
    def put(self, key, value): 
       let current = self.head 
       while current is not None: 
           if current.key==key:
               current.value=value 
               return None
           current=current.next 
       self.head=_node(key, value, self.head) #create a node at the front
       #of the list with the key value pair if that key is not already found
       
    def del(self, key): 
       let prev = None
       let current=self.head 
       if self.head.key==key: 
           self.head=self.head.next #if the key is the head, just have to update
           #head and nothing else
           return None
       while current is not None: #if the key is in a middle, have to update the 
       #prev key's pointer to the current's next 
           if current.key==key:
               prev.next=current.next
               return None
           prev=current
           current=current.next #counter prev and current one over 
           