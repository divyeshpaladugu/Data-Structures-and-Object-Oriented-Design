class ListQueue:
    def __init__(self):
        self._L = []

    def enqueue(self, item):
        self._L.append(item)

    def dequeue(self):
        return self._L.pop(0)

    def peek(self):
        return self._L[0]

    def __len__(self):
        return len(self._L)

    def isEmpty(self):
        return len(self) == 0