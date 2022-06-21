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
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def find_subtree(self, root: TreeNode) -> TreeNode:
        self.min_subtree = root
        self.min_sum = float('inf')

        self.subtree_sum(root)
        return self.min_subtree

    def subtree_sum(self, root):
        if root is None:
            return 0
        
        left_sum, right_sum = self.subtree_sum(root.left), self.subtree_sum(root.right)
        curr_sum = left_sum + root.val + right_sum

        if curr_sum < self.min_sum:
            self.min_sum = curr_sum
            self.min_subtree = root

        return curr_sum
    
    
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
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def find_subtree(self, root: TreeNode) -> TreeNode:
        min_subtree, min_sum, curr_sum = self.subtree_sum(root)
        return min_subtree

    def subtree_sum(self, root):
        if root is None:
            return None, float('inf'), 0

        left_min_subtree, left_min_sum, left_sum = self.subtree_sum(root.left)
        right_min_subtree, right_min_sum, right_sum = self.subtree_sum(root.right)
        curr_sum = left_sum + root.val + right_sum

        min_sum = min(left_min_sum, right_min_sum, curr_sum)
        if left_min_sum == min_sum:
            return left_min_subtree, left_min_sum, curr_sum
        if right_min_sum == min_sum:
            return right_min_subtree, right_min_sum, curr_sum
        return root, curr_sum, curr_sum
```
