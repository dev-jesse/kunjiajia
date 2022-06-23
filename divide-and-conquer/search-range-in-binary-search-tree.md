```python3
# Solution 1
from typing import (
    List,
)
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
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        result = []
        self.traversal(root, k1, k2, result)
        return result

    def traversal(self, root, k1, k2, result):
        if not root:
            return
        
        # If current value is less than or equal to k1, then no need to go further left
        if root.val > k1:
            self.traversal(root.left, k1, k2, result)
        # Only reason this goes in the middle is inorder traversal (left, root, right)    
        if k1 <= root.val <= k2:
            result.append(root.val)
        # If current value is greater than or equal to k2, then no need to get furhter right
        if root.val < k2:
            self.traversal(root.right, k1, k2, result)

# Solution 2
from typing import (
    List,
)
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
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        inorder = []
        self.get_inorder(root, inorder)
        result = [num for num in inorder if num in range(k1, k2 + 1)]
        return result

    def get_inorder(self, root, inorder):
        if not root:
            return
        self.get_inorder(root.left, inorder)
        inorder.append(root.val)
        self.get_inorder(root.right, inorder)
```
