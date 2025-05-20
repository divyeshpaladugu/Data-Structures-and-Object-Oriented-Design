# Assuming queue2050.py and stack2050.py are available and correctly implemented
from queue2050 import Queue
from stack2050 import Stack

class Graph:
    """Base class for graphs with common graph operations. Not meant to be instantiated directly."""
    def __init__(self):
        raise NotImplementedError("This class should not be instantiated directly")
    
    def connected(self, v1, v2):
        """Use BFS to check if there is a path from v1 to v2."""
        visited = set()
        q = Queue()
        q.enqueue(v1)
        while not q.is_empty():
            current = q.dequeue()
            if current == v2:
                return True
            visited.add(current)
            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    q.enqueue(neighbor)
        return False
    
    def bfs(self, v):
        """Perform a breadth-first search starting from vertex v."""
        visited = {}
        q = Queue()
        q.enqueue(v)
        visited[v] = None
        while not q.is_empty():
            current = q.dequeue()
            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    visited[neighbor] = current
                    q.enqueue(neighbor)
        return visited
    
    def dfs(self, v):
        """Perform a depth-first search starting from vertex v."""
        visited = {}
        stack = Stack()
        stack.push(v)
        visited[v] = None
        while not stack.is_empty():
            current = stack.pop()
            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    visited[neighbor] = current
                    stack.push(neighbor)
        return visited
    
    def has_cycle(self):
        """ Check if the graph contains a cycle using DFS. """
        def visit(v, parent, visited, stack):
            """ Helper function to visit nodes recursively. """
            if v in stack:
                return True  # Found a cycle
            if v in visited:
                return False
            
            visited.add(v)
            stack.add(v)
            for neighbor in self.neighbors(v):
                if neighbor != parent and visit(neighbor, v, visited, stack):
                    return True
            stack.remove(v)
            return False

        visited = set()
        for v in self.vertices():
            if v not in visited:
                if visit(v, None, visited, set()):
                    return True, []  # Currently returns True, cycle details need to be added
        return False, None
    
    def shortest_path(self, v1, v2):
        """Find the shortest path from v1 to v2 using BFS."""
        if v1 not in self.vertices() or v2 not in self.vertices():
            return (float("inf"), None)
        
        visited = {v1: None}
        q = Queue()
        q.enqueue(v1)
        
        while not q.is_empty():
            current = q.dequeue()
            if current == v2:
                break
            for neighbor in self.neighbors(current):
                if neighbor not in visited:
                    visited[neighbor] = current
                    q.enqueue(neighbor)
        
        if v2 not in visited:
            return (float("inf"), None)

        path = []
        step = v2
        while step != v1:
            parent = visited[step]
            path.append((parent, step))
            step = parent
        path.reverse()
        return (len(path), path)
    
    def vertices(self):
        raise NotImplementedError
    
    def neighbors(self, v):
        raise NotImplementedError

class AdjacencySetGraph(Graph):
    """Graph representation using adjacency set for efficient neighbor look-up."""
    def __init__(self, V=None, E=None):
        self.adj = {}
        if V:
            for v in V:
                self.add_vertex(v)
        if E:
            for u, v in E:
                self.add_edge(u, v)
    
    def __iter__(self):
        return iter(self.adj)
    
    def add_vertex(self, v):
        self.adj.setdefault(v, set())
    
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].add(v)
    
    def neighbors(self, v):
        return iter(self.adj.get(v, []))
    
    def vertices(self):
        return set(self.adj.keys())

class EdgeSetGraph(Graph):
    """Graph representation using edge set, suitable for dense graphs or frequent edge manipulations."""
    def __init__(self, V=None, E=None):
        self.vertices_set = set()
        self.edges = set()
        if V:
            for v in V:
                self.add_vertex(v)
        if E:
            for u, v in E:
                self.add_edge(u, v)
    
    def __iter__(self):
        return iter(self.vertices_set)
    
    def add_vertex(self, v):
        self.vertices_set.add(v)
    
    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.edges.add((u, v))
    
    def neighbors(self, v):
        return (v2 for u, v2 in self.edges if u == v)
    
    def vertices(self):
        return self.vertices_set
