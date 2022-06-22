```python3
# Solution 1 - Simple inorder traversal
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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        inorder_list = []
        self.dfs(root, inorder_list)
        return inorder_list[k - 1]

    def dfs(self, root, inorder_list):
        if not root:
            return
        self.dfs(root.left, inorder_list)
        inorder_list.append(root.val)
        self.dfs(root.right, inorder_list)
        
        
# Solution 2 - Tree Iterator
# ADVANCED: Need to memorise
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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kth_smallest(self, root: TreeNode, k: int) -> int:
        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]

        for _ in range(k):
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if not stack: return

        return stack[-1].val
```
