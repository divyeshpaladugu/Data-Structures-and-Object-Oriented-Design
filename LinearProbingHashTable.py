from UniqueLinkedList import UniqueLinkedList

class LinearProbingHashTable:
    def __init__(self, MINBUCKETS=2, MINLOADFACTOR=0.1, MAXLOADFACTOR=0.9):
        """Initializes the Linear Probing Hash Table."""
        self.MINBUCKETS = MINBUCKETS
        self.MINLOADFACTOR = MINLOADFACTOR
        self.MAXLOADFACTOR = MAXLOADFACTOR
        self.size = 0
        self.buckets = [None] * MINBUCKETS

    def __len__(self):
        """Returns the number of key-value pairs stored in the hash table."""
        return self.size
    
    def __setitem__(self, key, value):
        """Adds a key-value pair to the hash table."""
        index = hash(key) % len(self.buckets)
        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                self.buckets[index] = (key, value)
                return
            index = (index + 1) % len(self.buckets)
        self.buckets[index] = (key, value)
        self.size += 1

    def __getitem__(self, key):
        """Retrieves the value associated with the given key."""
        index = hash(key) % len(self.buckets)
        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                return self.buckets[index][1]
            index = (index + 1) % len(self.buckets)
        raise KeyError(key)

    def __contains__(self, key):
        """Checks if the given key exists in the hash table."""
        try:
            _ = self[key]
            return True
        except KeyError:
            return False

    def pop(self, key):
        """Removes the key-value pair associated with the given key from the hash table."""
        index = hash(key) % len(self.buckets)
        while self.buckets[index] is not None:
            if self.buckets[index][0] == key:
                self.buckets[index] = None
                self.size -= 1
                return
            index = (index + 1) % len(self.buckets)
        raise KeyError(key)

    def get_loadfactor(self):
        """Calculates and returns the load factor of the hash table."""
        return self.size / len(self.buckets)