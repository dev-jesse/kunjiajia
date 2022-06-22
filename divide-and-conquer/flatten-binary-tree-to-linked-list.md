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
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def flatten(self, root: TreeNode):
        return self.flatten_helper(root)

    def flatten_helper(self, root):
        if not root:
            return

        left_last = self.flatten_helper(root.left)
        right_last = self.flatten_helper(root.right)
        
        if left_last is not None:
            left_last.right = root.right
            root.right = root.left
            root.left = None

        return right_last or left_last or root
```
