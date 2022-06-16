```python3
# Solution 1 - O(n^2)
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def str_str(self, source: str, target: str) -> int:
        if source is None or target is None:
            return -1

        if len(target) == 0:
            return 0

        for i in range(len(source) - len(target) + 1):
            j = 0
            while (j < len(target)):
                if source[i + j] != target[j]:
                    break
                j += 1
            if j == len(target):
                return i

        return -1
        
# Solution 2 - O(mn)
UNDERSTAND HASHING BY RABIN KARP
```
