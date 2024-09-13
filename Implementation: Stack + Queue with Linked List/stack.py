class ListStack[T] (STACK):
let head

# Constructs an empty ListStack.
def __init__ (self):
    self.head = None

def empty?(self):
    if self.head == None:
        return True
    else:
        return False

def pop(self):
    if self.empty?():
        error("Can't pop from an empty list")
    let data = self.head.data
    self.head=self.head.next
    return data

def push(self, element):
    self.head=_cons(element, self.head)

#- empty?: If the head is empty, return true, otherwise false
#- Pop: Raises error if empty (can’t pop from empty list). Otherwise, store and return data that the head originally points to and then update that head pointer to the next node.
#- push: Update the heads pointer to a new node that has the new element and that points to the original head pointing node (places in between head and original first node essentially)