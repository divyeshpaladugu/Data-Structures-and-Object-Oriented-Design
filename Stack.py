class Stack:
    def __init__ (self):
        """Creates a new stack object"""
        self._L = []


    def __len__(self):
        """returns numebr of items in a stack"""
        return len(self._L)

    def is_empty(self):
        """returns true iff the stack is empty"""
        return len(self) == 0
    
    def push(self, item):
        self._L.append(item)

    def peek(self):
        return self._L[-1]

    def pop(self):
        return self._L.pop()