```python3
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        self.dfs(nums, 0, [], subsets)
        return subsets
        
    def dfs(self, nums, index, subset, subsets):
        if index == len(nums):
            subsets.append(subset.copy())
            return
        
        subset.append(nums[index])
        self.dfs(nums, index + 1, subset, subsets)
        
        subset.pop()
        self.dfs(nums, index + 1, subset, subsets)
```
