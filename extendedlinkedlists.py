from linkedlist import Node, LinkedList

class ReversableLinkedList(LinkedList):
    def reverse(self):
        """Reverse the direction of the Linked List"""
        current_node = self._head
        previous_node = None
        while current_node:
            next_node = current_node.link
            current_node.link = previous_node
            previous_node = current_node
            current_node = next_node
        self._tail, self._head = self._head, self._tail  # Swap head and tail

class SortedLinkedList(LinkedList):
    def add_sorted(self, item):
        """Add item to the linked list in sorted order"""
        new_node = Node(item)
        if not self._head or item <= self._head.item:  # if list is empty or item should be at the head
            new_node.link = self._head
            self._head = new_node
            if not self._tail:  # if list was empty, update _tail
                self._tail = new_node
        else:
            current_node = self._head
            previous_node = None
            while current_node and current_node.item < item:  # find insertion point
                previous_node = current_node
                current_node = current_node.link
            previous_node.link = new_node
            new_node.link = current_node
            if not current_node:  # if new_node is the last node, update _tail
                self._tail = new_node

    def add_first(self, item):
        """Add item to the beginning of the linked list."""
        raise NotImplementedError(f"Use add_sorted({item}) instead")

    def add_last(self, item):
        """Add item to the end of the linked list."""
        raise NotImplementedError(f"Use add_sorted({item}) instead")

    def __len__(self):
        """Return the number of elements in the linked list"""
        count = 0
        current_node = self._head
        while current_node:
            count += 1
            current_node = current_node.link
        return count

class UniqueLinkedList(LinkedList):
    def __init__(self):
        super().__init__()
        self._length = 0  # Initialize length attribute to zero

    def remove_dups(self):
        """Remove duplicate items from the linked list"""
        item_counts = {}
        current_node = self._head
        previous_node = None
        while current_node:
            if current_node.item in item_counts:
                item_counts[current_node.item] += 1
                previous_node.link = current_node.link
                if not current_node.link:  # if removed node was the tail, update _tail
                    self._tail = previous_node
                current_node = previous_node.link  # move to the next node without advancing previous_node
            else:
                item_counts[current_node.item] = 1
                previous_node = current_node
                current_node = current_node.link  # move to the next node
        
        # Identify items that need to be removed
        items_to_remove = [item for item, count in item_counts.items() if count > 1]
        
        # Remove items with count > 1 from the linked list
        for item in items_to_remove:
            current_node = self._head
            previous_node = None
            while current_node:
                if current_node.item == item:
                    if previous_node:
                        previous_node.link = current_node.link
                    else:
                        self._head = current_node.link
                    if not current_node.link:
                        self._tail = previous_node
                else:
                    previous_node = current_node
                current_node = current_node.link
        
        # Update the length of the linked list
        self._length -= len(items_to_remove)

        return item_counts
