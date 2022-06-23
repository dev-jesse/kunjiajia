```python3
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
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
             we will sort your return value in output
    """
    def closest_k_values(self, root: TreeNode, target: float, k: int) -> List[int]:
        nums = []
        self.dfs(root, nums)
        
        result = []
        index = self.binary_search(nums, target)
        left, right = index - 1, index

        for _ in range(k):
            if right == len(nums):
                result.append(nums[left])
                left -= 1
            elif left < 0:
                result.append(nums[right])
                right += 1
            else:
                if target - nums[left] < nums[right] - target:
                    result.append(nums[left])
                    left -= 1
                else:
                    result.append(nums[right])
                    right += 1

        return result

    def binary_search(self, nums, target):
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if target < nums[mid]:
                end = mid
            else:
                start = mid

        if nums[start] >= target:
            return start
        if nums[end] >= target:
            return end
        return len(nums)


    def dfs(self, root, inorder):
        if not root:
            return

        self.dfs(root.left, inorder)
        inorder.append(root.val)
        self.dfs(root.right, inorder)
```
