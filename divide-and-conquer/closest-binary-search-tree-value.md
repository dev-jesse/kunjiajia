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
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closest_value(self, root: TreeNode, target: float) -> int:
        if not root:
            return None

        upper = self.get_upper(root, target)
        lower = self.get_lower(root, target)

        # Example:
        #
        #       5
        #      / \
        #     4   9
        #    /   / \
        #   2   8  10
        # 
        #  Explanation for the below statements:

        if lower is None:
            # Target = 1.8, we cannot find a number <= 1.8 so return 2
            return upper.val
        if upper is None:
            # Target = 11
            return lower.val
        if target - lower.val < upper.val - target:
            return lower.val
        return upper.val

    def get_lower(self, root, target):
        if not root:
            return None

        # Move root until number is smaller than target
        if target < root.val:
            return self.get_lower(root.left, target)
        
        # Then move as tight to the target as possible going up
        lower = self.get_lower(root.right, target)
        return root if not lower else lower

    def get_upper(self, root, target):
        if not root:
            return None

        # Same logic as above, first go over the target value
        # and then move to the left
        if target >= root.val:
            return self.get_upper(root.right, target)

        upper = self.get_upper(root.left, target)
        return root if not upper else upper
```
