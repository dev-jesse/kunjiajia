```python3
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        permutations = []
        self.dfs(nums, [False] * len(nums), [], permutations)
        return permutations
    
    def dfs(self, nums, visited, permutation, permutations):
        if len(nums) == len(permutation):
            permutations.append(list(permutation))
        else:
            for i in range(len(nums)):
                if visited[i] or i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                visited[i] = True
                permutation.append(nums[i])
                self.dfs(nums, visited, permutation, permutations)
                permutation.pop()
                visited[i] = False
``
