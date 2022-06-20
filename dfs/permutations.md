```python3
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()  // Not needed but usually involved in solutions
        permutations = []
        self.dfs(nums, set(), [], permutations)
        return permutations
    
    def dfs(self, nums, visited, permutation, permutations):
        if len(permutation) == len(nums):
            permutations.append(list(permutation))
        else:
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                visited.add(nums[i])
                permutation.append(nums[i])
                self.dfs(nums, visited, permutation, permutations)
                permutation.pop()
                visited.remove(nums[i])
```
