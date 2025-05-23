class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.data})"

############################################
### Please do not alter the above class. ###
############################################

def height(t):
    if t is None:
        return -1
    else:
        return 1 + max(height(t.left), height(t.right))

def size(t):
    if t is None:
        return 0
    else:
        return 1 + size(t.left) + size(t.right)

def find_min(t):
    if t is None:
        return float("inf")
    else:
        return min(t.data, find_min(t.left), find_min(t.right))

def find_max(t):
    if t is None:
        return float("-inf")
    else:
        return max(t.data, find_max(t.left), find_max(t.right))

def contains(t, k):
    if t is None:
        return False
    elif t.data == k:
        return True
    else:
        return contains(t.left, k) or contains(t.right, k)

def in_order(t):
    result = []
    if t:
        result += in_order(t.left)
        result.append(t.data)
        result += in_order(t.right)
    return result

def pre_order(t):
    result = []
    if t:
        result.append(t.data)
        result += pre_order(t.left)
        result += pre_order(t.right)
    return result

def post_order(t):
    result = []
    if t:
        result += post_order(t.left)
        result += post_order(t.right)
        result.append(t.data)
    return result