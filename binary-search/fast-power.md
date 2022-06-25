```python3
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fast_power(self, a: int, b: int, n: int) -> int:
        if n < 0:
            n = -n
            a = 1 / a

        ans = 1
        while n:
            if n % 2:
                ans = ans * a % b
            a = a * a % b
            n //= 2

        return ans % b
```
