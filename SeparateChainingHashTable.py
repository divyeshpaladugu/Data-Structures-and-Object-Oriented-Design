from UniqueLinkedList import UniqueLinkedList

class SeparateChainingHashTable:
    def __init__(self, MINBUCKETS=2, MINLOADFACTOR=0.5, MAXLOADFACTOR=1.5):
        """Initializes the Separate Chaining Hash Table."""
        self.MINBUCKETS = MINBUCKETS
        self.MINLOADFACTOR = MINLOADFACTOR
        self.MAXLOADFACTOR = MAXLOADFACTOR
        self.size = 0
        self.buckets = [UniqueLinkedList() for _ in range(MINBUCKETS)]

    def __len__(self):
        """Returns the number of key-value pairs stored in the hash table."""
        return self.size
    
    def __setitem__(self, key, value):
        """Adds a key-value pair to the hash table."""
        index = hash(key) % len(self.buckets)
        self.buckets[index].add(key, value)
        self.size += 1

    def __getitem__(self, key):
        """Retrieves the value associated with the given key."""
        index = hash(key) % len(self.buckets)
        return self.buckets[index].get(key)

    def __contains__(self, key):
        """Checks if the given key exists in the hash table."""
        index = hash(key) % len(self.buckets)
        return key in self.buckets[index]

    def pop(self, key):
        """Removes the key-value pair associated with the given key from the hash table."""
        index = hash(key) % len(self.buckets)
        if key in self.buckets[index]:
            self.buckets[index].remove(key)
            self.size -= 1
        else:
            raise KeyError(key)

    def get_loadfactor(self):
        """Calculates and returns the load factor of the hash table."""
        return self.size / len(self.buckets)
