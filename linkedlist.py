class Node:
    def __init__(self, item, link = None):
        """Creates an empty node for a linked list
        
        Input
        -----
            item: Any
                Nodes can store any type of item
        
            link: Node or None
                Nodes link to either the next node, or (for the tail node) the None object
        """
        self.item = item
        self.link = link

    def __eq__(self, other):
        """Returns True iff self and other have the same item, regardless of their links
        Input
        -----
            self: Node
            other: Node
    
        Output
        ------
            : bool
        """
        return self.item == other.item
    
    def __repr__(self):
        """Returns machine-readable string representation of object

        repr() and str() both return string representations. repr() is called on an object when 
        a unittest fails, so it's good to explicilty implement this when debugging. Otherwise, you
        just get e.g. "Node object at 0x12984923187 not equal to Node object at 0x1289479981"

        Technical differences (outside the scope of 2050):
            * repr() should be *machine-readable* - the string it returns must have all information
                    needed to recreate the given object
        
            * str() should be *human-readable* - it only needs the information that is useful to a
                    human.
            
        These are often the same, but differ frequently enough for python to define two methods.
        
        Input
        -----
            self: Node
        
        Output
        ------
            : str
                string representation of object

        Examples
        --------
            >>> node1 = Node('Jake')
            >>> repr(node1) # includes class name, so object can be recreated
            Node(Jake)
            >>> str(node1) # readable by humans - does not necessarily need class name
            Jake
        """

        return f"Node({self.item})"

class LinkedList:
    def __init__(self, items=None):
        """Constructs a new linked list. If provided, items in `items` are iteratively added"""
        self._head = None
        self._tail = None
        self._len = 0

        if items:
            for item in items:
                self.add_last(item) # add to beginning to maintain order
        
    def __len__(self):
        """Returns number of nodes in linked list"""
        return self._len

    def get_head(self):
        """Returns item stored in first node if that node exists, otherwise None"""
        return self._head.item if self._head else None

    def get_tail(self):
        """Returns item stored in last node if that node exists, otherwise None"""
        return self._tail.item if self._tail else None
    
    def add_first(self, item):
        """Adds to start of LinkedList"""
        new_node = Node(item, link=self._head)
        self._head = new_node
        self._len += 1

        if len(self) == 1: self._tail = self._head # first node added

    def add_last(self, item):
        """Adds to end of LinkedList""" 
        new_node = Node(item)
        if self._tail: self._tail.link = new_node # general case: update tail.link
        self._tail = new_node
        self._len += 1

        if len(self) == 1: self._head = self._tail # first node added

    def remove_first(self):
        """Removes first node and returns its item"""
        if len(self) == 0:
            raise RuntimeError("Cannot remove from empty Linked List")
        
        item = self._head.item
        self._head = self._head.link
        self._len -= 1

        if len(self) == 0: self._tail = None

        return item

    def remove_last(self):
        """Removes last node and returns its item"""
        if len(self) == 0:
            raise RuntimeError("Cannot remove from empty LinkedList")
        
        elif len(self) == 1:
            return self.remove_first()

        # We have at least 2 nodes if we make it here
        item = self._tail.item
        
        # Find the penultimate (second to last) node
        new_tail = self._head
        while new_tail.link.link: new_tail = new_tail.link

        # Update pointers
        new_tail.link = None
        self._tail = new_tail

        # Update length
        self._len -= 1

        return item