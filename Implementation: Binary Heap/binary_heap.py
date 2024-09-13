interface PRIORITY_QUEUE[X]:
    # Returns the number of elements in the priority queue.
    def len(self) -> nat?
    # Returns the smallest element; error if empty.
    def find_min(self) -> X
    # Removes the smallest element; error if empty.
    def remove_min(self) -> NoneC
    # Inserts an element; error if full.
    def insert(self, element: X) -> NoneC

# Class implementing the PRIORITY_QUEUE ADT as a binary heap.
class BinHeap[X] (PRIORITY_QUEUE):
    let _data: VecC[OrC(X, NoneC)]
    let _size: nat?
    let _lt?:  FunC[X, X, bool?]
    let _capacity: nat? 

    # Constructs a new binary heap with the given capacity and
    # less-than function for type X.
    def __init__(self, capacity, lt?):
        self._size=0
        self._capacity = capacity
        self._data=[None for _ in range(capacity)]
        self._lt?=lt? 

# Other methods you may need can go here.
        
    def swap(self, index1, index2): 
        let temp = self._data[index1]
        self._data[index1]=self._data[index2]
        self._data[index2]=temp
        
    def bubble_up(self, index):
        while index > 0: 
            let parent_index=(index-1)//2
            if self._lt?(self._data[index], self._data[parent_index]):
                self.swap(index, parent_index)
                index=parent_index
            else:
                return 
       
    def percolate_down(self, index): 
        while index<self._size: 
            let left_child_index=(2*index)+1
            let right_child_index=(2*index)+2
            let smallest = None
            if left_child_index < self._size and right_child_index < self._size:
                if self._lt?(self._data[left_child_index], self._data[right_child_index]):
                    smallest = left_child_index
                else:
                    smallest = right_child_index
            elif left_child_index < self._size:
                smallest = left_child_index
            elif right_child_index < self._size:
                smallest = right_child_index
            if smallest is None: 
                return
            if self._lt?(self._data[smallest], self._data[index]):
                self.swap(smallest, index)
                index = smallest
            else:
                return 
            
              

    def len(self): 
        return self._size
        
    def find_min(self): 
        if self._size is not 0: 
            return self._data[0]
        else: 
            error("Empty Heap")
            
    def remove_min(self): 
        if self._size is not 0: 
            self._data[0]=self._data[self._size-1] 
            self._data[self._size-1] = None
            self._size = self._size - 1
            self.percolate_down(0)
        else: 
            error("Empty Heap")
            
    def insert(self, element): 
        if self._size>=self._capacity:
            error("Full Heap")
        else: 
            self._data[self._size]=element 
            self.bubble_up(self._size) 
            self._size=self._size+1 
            
    #Helper function for testing, retrieves the heap array 
    def get_heap_array(self):
        let heap_array = [None for _ in range(self._size)]
        for i in range(self._size):
            heap_array[i] = self._data[i]
        return heap_array
    

#1. len is just returning self.size. Note: self.capacity is how large the binheap is initialized to (empty array of size capacity). self.size is our actual size which gets updated +1 for insert and -1 for remove 
#2. find_min, return first element of array which is the min (this is how the bin heap operates, constant time for min element). Error if self.size is 0 (empty)
#3. remove_min: Replace the first (min) element with the last element which is self.data[0]=self.data[self.size-1]. Then, set that last element slot to empty and update size. Percolate down the new self.data[0] to restore heap. Removes min and restores heap. Error if self.size is 0 (empty)
#4. insert: insert the new element in the last slot of the array self.data[self.size]=element. Then bubble up that index to restore heap and then update size. Error if self.size≥self.capacity (full) 
#5. bubble_up and percolate_down just involve checking the lt? comparator with respective parent or child and swapping if true.