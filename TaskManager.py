class Entry:
    
    def __init__(self, priority, process_id):
        self.priority = priority
        self.process_id = process_id
    
    def __repr__(self):
        return f"Entry(priority={self.priority}, process_id={self.process_id})"

    def __gt__(self, other):

        return self.priority > other.priority

    def __eq__(self, other):

        return self.priority == other.priority

class MaxHeap:
    def __init__(self):
        """Initializes a MaxHeap object."""
        self._heap = []

    def put(self, entry):
        """Inserts an entry into the max heap."""
        self._heap.append(entry)
        self._upheap(len(self._heap) - 1)

    def remove_max(self):
        if not self._heap:
            raise IndexError("remove_max(): empty heap")
        last_item = self._heap.pop()
        if self._heap:
            return_item = self._heap[0]
            self._heap[0] = last_item
            self._downheap(0)
        else:
            return_item = last_item
        return return_item.process_id

    def change_priority(self, process_id, new_priority):
        for i in range(len(self._heap)):
            if self._heap[i].process_id == process_id:
                old_priority = self._heap[i].priority
                self._heap[i].priority = new_priority
                if new_priority > old_priority:
                    self._upheap(i)
                else:
                    self._downheap(i)
                return True
        return False

    def _upheap(self, index):
        parent = (index - 1) // 2
        if index > 0 and self._heap[index] > self._heap[parent]:
            self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]
            self._upheap(parent)

    def _downheap(self, index):
        child = 2 * index + 1
        if child < len(self._heap):
            right = child + 1
            if right < len(self._heap) and self._heap[right] > self._heap[child]:
                child = right
            if self._heap[child] > self._heap[index]:
                self._heap[index], self._heap[child] = self._heap[child], self._heap[index]
                self._downheap(child)

    def __len__(self):
        return len(self._heap)

class TaskManager:

    def __init__(self):
        """Initializes a TaskManager object."""
        self.processor_queue = MaxHeap()

    def add_process(self, entry):
        """Adds a process to the processor queue."""
        self.processor_queue.put(entry)

    def remove_process(self):
        """Removes and returns the process with the highest priority from the processor queue."""
        return self.processor_queue.remove_max()