```python3
# Solution 1
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
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def is_valid_b_s_t(self, root: TreeNode) -> bool:
        is_valid, _, _ = self.is_valid(root)
        return is_valid

    def is_valid(self, root):
        if not root:
            return True, None, None
        
        left_valid, left_min, left_max = self.is_valid(root.left)
        right_valid, right_min, right_max = self.is_valid(root.right)
        
        if not left_valid or not right_valid:
            return False, None, None
        if left_max and root.val <= left_max:
            return False, None, None
        if right_min and root.val >= right_min:
            return False, None, None
        
        right_max = right_max if right_max else root.val
        left_min = left_min if left_min else root.val

        return True, left_min, right_max
        
# Solution 2
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
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def is_valid_b_s_t(self, root: TreeNode) -> bool:
        stack = []
        while root:
            stack.append(root)
            root = root.left

        last_node = -float('inf')
        while stack:
            node = stack.pop()
            x = node.right
            while x:
                stack.append(x)
                x = x.left
            
            if last_node >= node.val:
                return False
            last_node = node.val
        
        return True
```
