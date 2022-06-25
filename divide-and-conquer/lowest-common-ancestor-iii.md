```python3
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        lca, a_found, b_found = self.lca_finder(root, A, B)
        return lca if a_found and b_found else None

    def lca_finder(self, root, a, b):
        if not root:
            return None, False, False
        
        left, left_a, left_b = self.lca_finder(root.left, a, b)
        right, right_a, right_b = self.lca_finder(root.right, a, b)

        a_found = left_a or right_a or a == root
        b_found = left_b or right_b or b == root

        if root == a or root == b:
            return root, a_found, b_found
        
        if left and right:
            return root, a_found, b_found
        if left:
            return left, a_found, b_found
        if right:
            return right, a_found, b_found

        return None, False, False
```
