# Introduction to Dynamic Programming

Dynamic programming is a technique that solves a problem by breaking it down into smaller subproblems, solving each of those subproblems just once and storing their solutions, then solving the original (bigger) problem by combining the solutions to the subproblems. It is best used when we want to compute optimal solutions to a sequence of problems where there exists overlapping subproblems.


## Coin-Row Problem
### Problem
There is a row of n coins whose values are positive integers c1, c2, . . . , , cn. The goal is
to pick up the maximum value subject to the constraint that no two coins adjacent in the
initial row can be picked up.

**Example**

```
Input = [5, 1, 2, 10, 6, 2]
Output = 17
```

### Solution
**Intuition**

The subproblem that we are trying to solve is at every position, what is the most amount of coins we could have collected up to this point.
Therefore, the entire problem really just boils down to two key questions
1. Would it be better to take the current coin + max amount of coins up to 2 positions ago
2. Take the coin from the previous house and the max coins before that

This should be a fairly easy recurrence to come up with, and should follow something like this
```
take_coins(i) = max(take_coins(i - 2) + current_coin, take_coins(i - 1))
```

**Code**
```python
def mario_top_down(coins):
    '''
    Mario like to take coins, hence the function name lol. Note that all
    top down solution that I show can have a memoization cache added to 
    optimize runtime (or slap a @lru_cache(None) decorator on lol).
    '''
    def take_coins(i):
        if i < 0:
            return 0
        return max(take_coins(i - 2) + coins[i], take_coins(i - 1))

    return take_coins(len(coins) - 1)

def mario_bottom_up(coins):
    '''
    Note that we can just use two variables prev and curr to save
    space. It should be fairly simple to implement, but if have
    any trouble feel free to contact me :)
    '''
    if len(coins) <= 2: return max(coins)

    dp = [0] * len(coins)
    dp[0] = coins[0]  # coins are positive so take it
    dp[1] = max(coins[0], coins[1]) # would it be better to take first or second coin
    for i in range(2, len(coins)):
        dp[i] = max(dp[i - 2] + coins[i], dp[i - 1])  # recurrence est. above
    
    return dp[-1]  # most coins that could be collected by last position
```

## Coin-Collecting Problem
### Problem
Each cell of an m×n board has 0 or 1 coin that can be picked up. A robot, located in
the upper left cell of the board (row 1, column 1), seeks to collect as many of the coins as
possible and bring them to the bottom right cell. On each step, the robot can make one
of two moves from its current location: move one cell to the right or move one cell down.
Design an algorithm to find the maximum number of coins the robot can collect and a path
that achieves this maximum.

**Example**
```
Input = [[0, 1, 1, 0, 0],
         [0, 1, 0, 0, 0],
         [1, 0, 0, 1, 1]]

Output = 4
```

### Solution
**Intuition**

The subproblem that we want to solve here is, at any position, what is the most amount of coins I could've
collected coming only from positions to the top or the left of my current position. Hence, at any position
1. Does the top hold a more optimal solution?
2. Does the left hold a more optimal solution?

Again, this should be fairly easy to convert into a recurrence
```
collect_coins(i, j) = max(collect_coins(i - 1, j), collect_coins(i, j - 1)) + current_coin_value
```

**Code**
```python
def robot_top_down(matrix):
    '''
    The robot is traversing the matrix to collect as many coins
    as they possibly can.
    '''
    n, m = len(matrix), len(matrix[0])

    def collect_coins(i, j):
        if i < 0 or j < 0:
            return 0
        return max(collect_coins(i - 1, j), collect_coins(i, j - 1)) + matrix[i][j]

    return collect_coins(n - 1, m - 1)

def robot_bottom_up(matrix):
    '''
    The robot got tired of recomputing his past answers and decided
    to put them in a array. Again, if you want to save space you can
    just use a single array of size O(m) and just roll top values down,
    but it should be fairly easy to implement. If you have issues with
    implementing it feel free to contact me :)
    '''
    n, m = len(matrix), len(matrix[0])
    # Need an extra row and col to keep indexing in range
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # Note: matrix[i - 1][j - 1] since we added extra row and col
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + matrix[i - 1][j - 1]

    return dp[n][m]
```

## Maximum Square Submatrix
### Problem
Given an m×n matrix B where each cell is 0 or 1, find its largest square submatrix whose
elements are all 0’s.

**Example**
```
Input = [[1, 0, 1, 0, 0],
         [1 ,0 ,1 ,1 ,1],
         [1, 1, 1, 1, 1],
         [1, 0, 0, 1, 0]]
Output = 4
```

### Solution
**Intuition**

From here on out, I will not be showing the top-down solution, since it is basically expressed by the 
intuition presented. If you have any troubles and would like to see the top-down solutions, just give me
a quick message and I will give it to you.

The intuition for this problem is slightly more tricky, but can be illustrated if we use a few small cases
to understand what makes a "square".
```
1 1  <- square
1 1 

0 1  <- not square
0 1

1 0
1 1  <- not square
```
From the examples above, what we notice is that all boxes in a square must be filled (1) in order to be a square.
Hence, we can check to our top-left, left, and top indices and see if they are filled, in order to check if we
are a square. This would lead to the following recurrence
```
side_length(i, j) = min(side_length(i - 1, j),
                        side_length(i - 1, j - 1)
                        side_length(i, j - 1)) + 1
```
Where this recurrence is **only checked under the condition that the current position is filled**. Notice that 
this is a recurrence to find the maximal side length of the square, so we need to return `side_length(i, j) * side_length(i, j)`

**Code**
```python
def maximal_square(matrix):
    '''
    困佳佳
    '''
    n, m = len(matrix), len(matrix[0])
    longest_side = 0
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i - 1][j - 1] != 1: continue                
            dp[i][j] = min(dp[i - 1][j], 
                            dp[i - 1][j - 1],
                            dp[i][j - 1]) + 1
            longest_side = max(longest_side, dp[i][j])
            
    return longest_side * longest_side
```

## Baseball Odds

### Problem 
Consider two teams, A and B, playing a series of games until one of the teams wins n
games. Assume that the probability of A winning a game is the same for each game and
equal to p, and the probability of A losing a game is q = 1−p. Let P(i, j) be the probability
of A winning the series when A needs i more games to win the series and B needs j
more games to win the series. Given the maximum number of games in a series (e.g. 7)
and a value of p (e.g. 0.4), find the probability of A winning the series.

**Example**
```
    games   p
        v   v
Input = 7, 0.4
Output = 0.2288439525376001
```

### Solution
**Intuition**
This question was confusing to me at first, however once you understand the main idea of the
question the recurrence becomes prevalent. Hopefully I can illustrate this through an example
```
1 game => p is the change to win
2 games => there are 3 ways to win, and 3 ways to lose

in fact, 2 games can go like this,
2, 2 -> 1, 2 (A wins 1) -> 1, 1 (B wins 1) -> 1, 0 (B wins 2)
2, 2 -> 2, 1 (A wins 2) -> 1, 1 (A wins 1) -> 1, 0 (B wins 2)
so although (1, 0) ending result happens, there are multiple ways to reach it
further, winning consecutive games makes p smaller
```
which can lead us to the following recurrence (provided base cases)
```python   
def baseball_odds(gamesA, gamesB, p):
    if gamesB == 0: return 0  # There is no way to win anymore
    if gamesA == 0: return 1  # We win the game 
    return baseball_odds(gamesA - 1, gamesB, p) * p + \
           baseball_odds(gamesA, gamesB - 1, p) * (1 - p)
```

**Code**
```python
def baseball_odds(games, p):
    '''
    Someone use this to bet on NBA finales and lmk how it go lol
    '''
    dp = [[0] * (games + 1) for _ in range(games + 1)]
    for i in range(1, games + 1):  # i represent number of games A wins
        dp[i][0] = 0
    for j in range(1, games + 1):  # j represent number of games B wins
        dp[0][j] = 1
    
    for i in range(1, games + 1):  # recurrence described ok
        for j in range(1, games + 1):
            dp[i][j] = dp[i - 1][j] * p + dp[i][j - 1] * (1 - p)
            
    return dp[games][games]
```