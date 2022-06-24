```python3
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of the binary search tree.
    @param value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def remove_node(self, root: TreeNode, value: int) -> TreeNode:
        if not root:
            return root
        
        # Remove from left subtree
        if value < root.val:
            root.left = self.remove_node(root.left, value)
        # Remove from right subtree
        elif value > root.val:
            root.right = self.remove_node(root.right, value)
        # We found the value as our current node
        else:
            # If there is no children then just remove
            if not root.left and not root.right:
                root = None
            # If there is a left child just exchange predeccessor
            elif root.left:
                root.val = self.get_predeccessor(root.left)
                root.left = self.remove_node(root.left, root.val)
            # If there is a right child just exchange successor
            else:
                root.val = self.get_successor(root.right)
                root.right = self.remove_node(root.right, root.val)        
        return root

    def get_successor(self, root):
        while root.left:
            root = root.left
        return root.val

    def get_predeccessor(self, root):
        while root.right:
            root = root.right
        return root.val
```
