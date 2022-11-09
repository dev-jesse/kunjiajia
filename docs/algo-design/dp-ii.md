# Introduction to Dynamic Programming II

## No Consecutive 1s
### Problem
For positive integer n, return the number of binary strings of length n that have no adjacent
1s.

**Example**
```
Input = 2
Output = 3
```

### Solution
**Intuition**

If we think of the base case, we know that a binary string of length 1 can only be two values, either '0' or '1'. Hence,
if there is a binary string of length 2 we know that for the '0', we can append either '0' or '1' but for the '1' we
must append a '0' otherwise we violate the condition. Below, we will visualize it for `n = 2`
```
        0        1
       / \        \      
     00  10        01   
```
hence allowing us to come with up recurrence
```
a[i] = number of binary strings of length i without consecutive ones ending in 0
b[i] = number of binary strings of length i without consecutive ones ending in 1

a[i] = a[i - 1] + b[i - 1]
b[i] = a[i - 1]
```

**Code**
```python
def not_consecutive(n):
    '''
    Note: You can make this constant space using a and b set to
    1, which is fairly simple since the rest of the implementation
    stays the same. Feel free to contact if you are struggling with
    this :)
    '''
    a = [0] * n
    b = [0] * n
    a[0] = b[0] = 1  # binary strings '1' and '0'
    for i in range(1, n):
        a[i] = a[i - 1] + b[i - 1]
        b[i] = a[i - 1]
    
    return a[n - 1] + b[n - 1]
```

## How Many Strings?
### Problem
For all integer values of n and k, let f (n, k) be the number of binary strings of length n
that have k more 1s than 0s. Develop a dynamic-programming algorithm to return f (n, k).
Here’s an example: f (2, 0) = 2. f (2, 0) should return the number of binary strings of
length 2 that have 0 more 1s than 0s (i.e. the same number of 1s and 0s). There are only
2 such strings: 10 and 01.
Another example: f (4, 1) = 0: there are no binary strings of length 4 that have one
more 1 than 0.

**Example**
```
        n k
        v v
Input = 2 0
Output = 2
```

### Solution
**Intuition**

Taken from the solutions pdf 

When n=0, we have one string when k=0 (the empty string), but no strings 
for any other k. For example, f(0,1) must be 0, because there is no string 
of length 0 that has one more 1 than 0.
Now consider strings of length n > 0. There are two choices for the last 
character of such strings. If the last character is a 0, then the first n-
1 characters must have k+1 more 1s than 0s for the entire string to have k 
more 1s than 0s. On the other hand, if the rightmost character is a 1, 
then the first n-1 characters must have k-1 more 1s than 0s. This leads to 
the following recursive definition:
```
f(n,k) = 1, if n = 0 and k = 0
0, if n = 0 and k != 0
f(n - 1, k + 1) + f(n - 1, k - 1), if n >= 1
```

**Code**
```python
def dyn(n, k):
    if k < 0: k = -k
    if k > n: return 0
    N = [[0 for _ in range(n+1)] for _ in range(n+1)]
    N[0][0] = 1
    for j in range(1, n+1):
        N[0][j] = 0
    for i in range(1, n+1):
        for j in range(n+1):
            if i == 0 and j == 0: continue
            if j == n:
                N[i][j] = N[i - 1][j - 1]
            elif j == 0:
                N[i][j] = N[i - 1][j + 1] + N[i - 1][1]
            else:
                N[i][j] = N[i - 1][j + 1] + N[i - 1][j - 1]
    return N[n][k]
```

## Longest Decreasing Subsequence
### Problem
Let S be a sequence of integers. A subsequence of S is produced by taking some
elements from left to right from S. For example, 2, 1 is a subsequence of 2, 5, 6, 1. A
decreasing subsequence is a subsequence whose elements are in decreasing order;
for example, 2, 1 is a decreasing subsequence, but 3, 3 is not.
The Longest Decreasing Subsequence (LDS) problem is to find the longest decreasing
subsequence of S. Solve this problem.

**Example**
```
Input = [2, 5, 6, 1]
Output = 2
```

### Solution
**Intuition**

This is a pretty classical problem in dynamic programming. I strongly suggest to watch a 
video on Longest Increasing Subsequence (LIS) to fully understand! There are also other
ways like using binary search but for the most part the `O(n^2)` should suffice.

**Code**
```python
def longest_decreasing(nums):
    '''
    Pretty classical DP. It is kinda late rn lol I wanna sleep.
    '''
    n = len(nums)
        dp = [1] * len(nums)  # Element itself is still subseqence
        for i in range(n):
            for j in range(i):
                if nums[i] < nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        
        return max(dp)
```