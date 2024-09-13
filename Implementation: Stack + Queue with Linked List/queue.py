class ListQueue[T] (QUEUE):
let head
let tail

# Constructs an empty ListQueue.
def __init__ (self):
    self.head = None
    self.tail = None

def empty?(self):
    if self.head == None:
        return True
    else:
        return False

def enqueue(self, element):
    if self.tail == None:
        let new = _cons(element, None)
        self.head = new
        self.tail = new
    else:
        self.tail.next = _cons(element, None)
        self.tail = self.tail.next

def dequeue(self):
    if self.empty?():
        error("Can't dequeue from an empty queue")
    let data
    if self.head==self.tail:
        data=self.head.data
        self.head=None
        self.tail=None
        return data
    else:
        data = self.head.data
        self.head=self.head.next
        return data


#- Queue needs a head and a tail
#- empty? True if head is None (tail will be none in this case too)
#- enqueue: Adding to the BACK so we use tail. If empty linked list (tail is none), we set both the head and tail to a new empty list. Usual case: Set the tails pointer to a new node that has the new element and that links to nothing (back of linked list node)
#- dequeue: Removing form the FRONT so we use head. Can’t dequeue from empty. If there’s only one node (head = tail), set both to none (remove) and return the data stored in the head/tail. Usual case: Change head’s pointer to the next node and return the data of the original removed node (that head pointed to)