class HashTable[K, V] (DICT):
    let _hash #hash function 
    let _size #number of key value pair mappings in the dict
    let _data #n buckets where each bucket is an association list
    let nbuckets #number of buckets 
    
    def __init__(self, nbuckets: nat?, hash: FunC[AnyC, nat?]):
        self._hash = hash
        self._size = 0 
        self._data = [AssociationList() for _ in range(nbuckets)]
        self.nbuckets = nbuckets
    # This avoids trying to print the hash function, since it's not really
    # printable and isn’t useful to see anyway:
    def __print__(self, print):
        print("#<object:HashTable  _hash=... _size=%p _data=%p>",
              self._size, self._data)

    def len(self):
        return self._size 
     
    def update_size(self):
        let s = 0
        for i in range(self.nbuckets): #Iterates through the bucket numbers
            s = s + self._data[i].len() #Adds the length of each bucket
            #indexed by the bucket number
        self._size = s #updates size 
        
    def mem?(self, key):
        let index = self._hash(key) % self.nbuckets #hash function assigns key
        #a hash code and then modulo it by the number of buckets for the 
        #final bucket index 
        return self._data[index].mem?(key) #since accessing the index of data
        #is an association list, call already written mem?() method on the key
        
    def get(self, key):
        let index=self._hash(key) % self.nbuckets 
        return self._data[index].get(key) #same thing as above? 
        
    def put(self, key, value):
        let index=self._hash(key) % self.nbuckets 
        self._data[index].put(key, value) #same thing as above
        self.update_size() #for put and del, need to update size afterwards 
       
    def del(self, key):
        let index=self._hash(key) % self.nbuckets 
        self._data[index].del(key) #same thing as above
        self.update_size()
#Second try notes: del has to check if the key is a mem first. If it isn't,
#do nothing(pass), ensures size isn't updates wrongly. 
#update size should just be +1 if something is put and -1 if something is 
#deleted. The update_size above is O(n) (has to iterate through every element)
#when it should just be O(1). Revised put and del: 

    def put(self, key, value):
        let index=self._hash(key) % self.nbuckets 
        if self._data[index].mem?(key):
            self._data[index].put(key, value)
        else:
            self._data[index].put(key, value)
            self._size = self._size + 1
       
    def del(self, key):
        let index=self._hash(key) % self.nbuckets 
        if self._data[index].mem?(key):
            self._data[index].del(key)
            self._size = self._size - 1
        else:
            pass