<!-- ## Canadian Coins

### Problem

**Example**

```

```

### Solution

**Intuition**

**Code** -->

# Greedy Coin Changing

Greedy algorithms are those which are inclined to take the shortest path or make the largest number of decisions. It iteratively makes one greedy choice after another, reducing each given problem into a smaller one.

## Canadian Coins

### Problem

You have an unlimited supply of 1c, 5c, 10c and 25c coins, and you want to make change for A cents
using as few coins as possible. For example, if you want to make change for 15c, then the best you can
do is use one 10c and one 5c coin. That’s better, for example, then using 15 1c coins.

**Example**

```
Input = 15
Output = 2
```

### Solution

**Intuition**

Taking a look at the supply of coins that we are given, it should be easy to see that all the larger valued coins (like 25c) can be constucted with the lower valued coins. This means that we want to take the larger valued coins as our first option as opposed to a smaller valued coin, since several of the smaller valued coin would make up the same value. For example, if we wanted to make 24c, then we should take the largest coins that are less or equal to 24c, which in this case would be the 10c. You will soon see, however, that this intuition is incorrect, but does hold for canonical coin systems.

**Code**

```python
def greedy_coin(desired_value):
    '''
    Mr. Krabs algorithm
    '''
    # ans array in case you want to keep track of coins used lol
    # you can use initialize ans = 0 if you just want to track number of coins
    ans = []
    # Order the coins non-increasingly
    coins = [25, 10, 5, 1]
    for i in range(len(coins)):
        # Reached the coins needed to meet desired value (return earlier)
        if desired_value == 0:
            return len(ans)
        while desired_value >= coins[i]:
            desired_value -= coins[i]
            ans.append(coins[i])

    # Return the total number of coins that we used
    return len(ans)
```

## New Coins

### Problem

Suppose now that we have the following types of coins: 1c, 5c, 10c, 26c.
Show that the greedy algorithm is not optimal in this case.

**Greedy Fails!**

```
Say we want to make 30c then,
Greedy: 26 + 1 + 1 + 1 = 4 coins
Optimal: 10 + 10 + 10 = 3 coins
```

**Example**

```
Input: 30
Output: 3
```

### Solution

**Intuition**

We realize that to get any coin, up to our desired amount, that they are composed of smaller sub problems. Namely, that if we can minimum amount of coins needed for a smaller
subproblems, that we can compute our larger subproblems off of it. For example, lets say we wanted to make 12c, then if we give 10c to the total amount, we just need to know the minimum number of coins it takes to make 2c, which should be computed in a smaller subproblem.

**Code**

```python
def dp_coins(coins=[1, 5, 10, 26], amount) -> int:
    '''
    Mr. Krabs 2.0

    I set coins to a default value so you guys can try different
    coin systems if you want lol.
    '''
    # dp[i] is the min amount of coins to make $i
    dp = [float('inf')] * (amount + 1)
    # 0 coins needed to make $0
    dp[0] = 0
    for i in range(amount + 1):
        for j in range(len(coins)):
            # if our current coin > $i, then skip it
            if coins[j] > i: continue
            # otherwise, 1 (current coin) + dp[i - coins[j]]
            # will be the number of coins it will take to make
            # the value including our current coin
            dp[i] = min(dp[i], 1 + dp[i - coins[j]])

    # return the minimum it takes to make $amount
    return dp[-1] if dp[-1] != inf else -1
```

## But why?

I will dedicate this last section for a few on why this algorithm works for certain sets of coins but not others. Firstly, it does work for canonical coin systems, and if you want a really in depth read/proof, then feel free to check out the post [here](https://arxiv.org/pdf/0809.0400.pdf).

The reason that only certain coin systems work, are because of [matroids](https://en.wikipedia.org/wiki/Matroid). The rigourous discussion can be found on StackOverflow [here](https://stackoverflow.com/questions/13557979/why-does-the-greedy-coin-change-algorithm-not-work-for-some-coin-sets). It looks like there is lots of debate on this topic, so if you have any questions be sure to ask the TAs and check the tutorial solutions!
