![image](https://user-images.githubusercontent.com/83730324/175786719-7680a3ac-5083-4d16-93e8-a70b4ba31ffd.png)
```python3
# Image displayed above is called fast power algorithm, good and easy to memorize
class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x * x, (n - 1) // 2)
        return self.myPow(x * x, n // 2)
        
# Solution 2 - Iterative (faster but logically hard to understand)
class Solution:
    def myPow(self, x, n):
        if n < 0:
            n = -n
            x = 1 / x
            
        ans = 1
        while n:
            if n % 2:
                ans *= x
            x *= x
            n //= 2
            
        return ans
```
