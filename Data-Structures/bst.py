class BSTNode:
    def __init__(self, value=None, left=None, right=None):
        self. value = value # Interestingly, there's an 'assumedness' that, well actually isn't an assumption-
        self.left = left    # There's no way to access a node in a binary tree, except from the root node (the head in Linked List speak),
        self.right = right  # meaning we don't have to indicate that we want to start insertion processes from the root- we can just assume they do.

    def insert(self, value):
        if self.value is None: # If there's no value in the tree, we insert the value into the root node.
            self.value = value
        elif self.value > value: # Else, we've met a condition that there are elements in the tree,
            if self.left:        # and thus, need to begin searching for a place to insert a value,
                                 # according to the binary tree property (nodes less than root on the left, greater than on the right)
                self.left.insert(value) # We can then initiate the insertion process recursively, as the structure of the binary tree
                                        # permits us to search the whole tree, via a node, and it's immediate sub-tree (the left and right nodes),
                                        # which is amenable to recursive solving, because it's a smaller version of the problem, and workload.
            else: # if there's not a self.left node, park it
                node = BSTNode(value)
                self.left = node
        elif self.value <= value:
            if self.right:
                self.right.insert(value)
            else: # if there's not a self.right node, park it
                node = BSTNode(value)
                self.right = node
    def minValNode(self, node):
        #  Recursively traverse left sub-tree.
        curNode = node
        while (curNode.left is not None):
            curNode = curNode.left
        return curNode
    
    def maxKey(node):
        while node.right:
            node = node.right

        return node
    def remove(self, value): 
            if self.value is None:
                return -1
            elif self.value > value:
                # we want to search the right sub-tree
                self.left = self.left.remove(value)
            elif self.value < value:
                    self.left = self.remove(value)
                    # we want to search the left sub-tree
            else:
                if self.left is None and self.right is None:
                    # This handles the case that the node we're on, 
                    # has no children.
                    return None
                elif self.right and self.left:
                    # In the event that there are children in either direction:
                    maxChild = self.maxKey(self.left)
                    # Grab the highest left sub-tree's child node, as the highest sub-child will be in the 
                    # lowest level of the tree, and since
                    self.value = maxChild.value
                    self.left = self.remove(self.left, maxChild.value)
                else:
                    child = self.left if self.left else self.right
                    # Find the child node to fill the spot of the deleted node.
                    self.root = child
            
    def contains(self, value):
        if self.value == value: # If the value is the value contained in the head node, we return true.
                               # We do this at the outset, because it's an `edge case`: usually we search inside of something,
                               # and don't expect it to be the first item we check, but this may be the case sometimes.
                                    # (This doesn't, however, factor into run-time, because we don't know when the item we're
                                    # looking for will be the first item, and also, run-time is about `worst-case` scenario's, which this
                                    # is certainly not- it's best case.)
            return True
        else:
            if self.value >= value: # In the event that we do have to search, we can compare the search value, to the nodes values,
                                   # according to the BST property- if the value is greater than the node value, we only have to look at the right sub-tree,
                                   # if it's less than, we search the left sub-tree.
                                        # This is why BST's have O(log n) time complexity for operations- they can generally decrease the search space
                                        # by 50% each iteration, as stated above
                if not self.left: # If there's no left sub-tree to search, however, then we can return false,
                                  # as the only section of the tree that could contain the value, is empty (technically non-existent)
                    return False
                else: # Here's where we initiate recursion to search the rest of the tree.
                   return self.left.contains(value)
            elif self.value <= value:
                    if not self.right:
                        return False
                    else: # Initiate recursion to search the rest of the tree.
                        return self.right.contains(value)
        return False
    def for_each(self, cb):
        if self.left is None and self.right is None:
            # If there are no child nodes,
            cb(self.value) # Apply the function to the root, and return
            return
        elif self.left or self.right: # If there are child nodes,
            if self.left: # If there's a left child,
                cb(self.value) # Apply the function to the value,
                self.left.for_each(cb) # Recurse through the sub-tree
            if self.right:
                cb(self.value)
                self.right.for_each(cb)

BST = BSTNode()

BST.insert(50)
BST.insert(90)
BST.insert(13)
BST.for_each(print)
print(BST.contains(150))
BST.remove(13)
print(BST.contains(13))
BST.for_each(print)


