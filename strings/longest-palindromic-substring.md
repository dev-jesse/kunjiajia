```python3
class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longest_palindrome(self, s: str) -> str:
        # write your code here
        res = ""
        for mid in range(len(s)):
            if len(self.get_palindrome(s, mid, mid)) > len(res):
                res = self.get_palindrome(s, mid, mid)
            if len(self.get_palindrome(s, mid, mid + 1)) > len(res):
                res = self.get_palindrome(s, mid, mid + 1)

        return res

    def get_palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and \
        s[left] == s[right]:
            left, right = left - 1, right + 1

        return s[left + 1: right]
```
