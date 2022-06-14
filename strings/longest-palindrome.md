```python3
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longest_palindrome(self, s: str) -> int:
        # write your code here
        char_count = collections.Counter(s)
        
        res = 0
        for value in char_count.values():
            res += value // 2 * 2
            if res % 2 == 0 and value % 2 == 1:
                res += 1
        
        return res
```
