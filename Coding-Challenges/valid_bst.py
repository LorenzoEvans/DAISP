""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    
    # Alright, so we want to make sure this tree,
    # conforms to the BST property, wherein all values higher
    # than the root node value are in the right sub-tree,
    # and the all values lower, in the left sub-tree,
    # where every node in the tree, follows these rules as well.
    
    # We know a greedy algorithm won't work, because this a 2D
    # data structure, and a greedy algorithm is a 1D algorithm:
    # it won't consider breadth and depth- only one of the two.
    
    # Edge cases
    if root is None:
        # If the root is none, we return -1
        return False
    elif not root.left and not root.right:
        # If there are no left or right child nodes, but just root
        # we return true, as a root node is technically a valid BST.
        return True
    if root.left or root.right:
        # If there is a left, or right node,
        root_node = root # We store the root node in a variable, for comparison
                            # later on
        if root_node.left:
            # If there's a left child
            l_node = root_node.left
            # We store that in a variable, as a target to recurse upon
            if l_node.data >= root_node.data:
                # If the value of this left sub-tree node, is higher than
                # the value of the root node, we know the tree is invalid.
                return False
            elif l_node.data <= root_node.data:
                # Otherwise, the tree is valid so far,
                root = l_node # we set root to our current node, and recurse
                return check_binary_search_tree_(root)
                # We return the recursion so that eventually,
                # our true or false value discovered by it will be available.
        elif root_node.right:
            # If there is a right child,
            r_node = root_node.right # we store that in a variable as well
            if r_node.data < root_node.data:
                # If the value in that node is less than the root node,
                # we know the tree is invalid.
                return False
            elif r_node.data > root_node.data:
            # Otherwise, the tree is valid so far,
                root = r_node # we set the root to our current node, and recurse
                return check_binary_search_tree_(root)
                # We return the recursion so that eventually,
                # our true or false value discovered by it will be available.
    return True