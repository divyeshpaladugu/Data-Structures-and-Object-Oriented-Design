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

def count_failures(pred, t):
    if t is None:
        return 0
    else:
        failed = not pred(t.data)
        return failed + count_failures(pred, t.left) + count_failures(pred, t.right)

def tree_map(f, t):
    if t is None:
        return None
    else:
        new_left = tree_map(f, t.left)
        new_right = tree_map(f, t.right)
        return TreeNode(f(t.data), left=new_left, right=new_right)

def tree_apply(f, t):
    if t is not None:
        t.data = f(t.data)
        tree_apply(f, t.left)
        tree_apply(f, t.right)