import random

class ListHash:
    
    def __init__(self, initialSize, p = 109234121):
        self._HashTable = initialSize * [None]
        self._size = 0
        self._prime = p
        self._scale = 1 + random.randrange(p-1)
        self._shift = random.randrange(p)

    def hash(self, x):
        # a hush function that converts a string x to an integer i.e. index 
        # in the hastable
        return (hash(x)*self._scale + self._shift) % self._prime % len(self._HashTable)

    def insert(self, x):
        # inserts string x to the HashTable in the index returned by hash(x)
        key, value = x
        bucket = hash(key)

        # if the hash table is more than half full, resize
        if self._size > (len(self._HashTable)/2):
            self._resize(2 * len(self._HashTable) - 1)

        # linear probing collision resolution. Loop until finding an open bucket
        while True:
            if self._HashTable[bucket] is None:
                self._HashTable[bucket] = x
                break
            # search the next bucket, accounting for cylcical data structure
            bucket = (bucket + 1) % len(self._HashTable)

        # update the size
        self._size += 1

    def size(self):
        # returns the size of the elements i.e. number of keys
        return self._size

    def _resize(self, new_size):
        currTable = self._HashTable
        self._HashTable = new_size * [None]

        # reinsert all the elements back into the newly sized table
        for x in currTable:
            self.insert(x)