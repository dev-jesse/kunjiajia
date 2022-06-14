```python3
# Solution 1
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                next_i, next_j = self.get_min_index(mat, i, j)
                mat[i][j], mat[next_i][next_j] = mat[next_i][next_j], mat[i][j]
                
        return mat
                
    def get_min_index(self, mat, i, j):
        min_item = mat[i][j]
        min_index = (i, j)
        
        while i in range(len(mat)) and \
        j in range(len(mat[0])):
            curr_item = mat[i][j]
            min_item = min(curr_item, min_item)
            
            if curr_item == min_item:
                min_index = (i, j)
                
            i, j = i + 1, j + 1
            
        return min_index
        
# Solution 2
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)
        
        # O(m * n)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[j - i].append(mat[i][j])
                
        # O(m * n * lg min(m, n))
        for key in d:
            d[key].sort(reverse=True)
            
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] = d[j - i].pop()
                
        return mat
```
