# Computation Complexity
> "Controlling complexity is the essence of computer programming." - Brian Kernigan

If you have ever taken any data structures course whether it be virtual or in person, chances are that you have experienced an idea called computational complexity. Usually, they are discussed in two separate parts: time complexity and space complexity. In interviews, the questioning of space complexity is usually trivial, since it is fairly easy to count the amount of objects created and the space taken from the creation of such objects. Time complexity on the other hand is slightly more difficult to estimate, and shows that you have a deep understanding on how to optimize and improve performance of existing code. In this section I will take a deep dive into computation complexity and what to focus on to practice for interviews.

## Big-O (+ other bounds)
Big-O notation is a mathematical notation that describes the limiting behavior of a function when the argument tends towards a particular value or infinity (as per [Wikipedia](https://en.wikipedia.org/wiki/Big_O_notation)). It is denoted by O(...). If you are interested in learning about lower bounds and strict bounds of algorithms, read about [Big-Omega](https://www.freecodecamp.org/news/big-omega-notation/) and [Big-Theta](https://www.freecodecamp.org/news/big-theta-and-asymptotic-notation-explained/) (written by the great authors at [freecodecamp](https://www.freecodecamp.org/)), respectively.

<img src="https://cdn-media-1.freecodecamp.org/images/05O9lIJ7IskYF05LomQMNSdgLSxE4qhY3xef">

## Space Complexity
Space complexity refers to the amount of memory space that a algorithm exhausts. This is usually simple in the case of interviews, as demonstrated in the example that follows:
```py
# Two Sum Solution
def twoSum(nums, target):
    hashmap = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in hashmap:
            return [i, hashmap[difference]]
        hashmap[num[i]] = i
```

Clearly, a hash table is created which will consume memory. In the worst case, every single number except for the last number is inserted into the hash table (with the assumption that `nums` contains at least one pair of numbers that add up to `target`). Therefore, the space complexity of the algorithm is `O(n -  1) = O(n)` (continue reading to see why we drop the constant or view rigorous explanation [here](https://stackoverflow.com/questions/59459899/space-complexity-dropping-the-non-dominant-terms)).

## Time Complexity
Time complexity is an approximation of how long an algorithm will take to process some given input. In other words, it describes the performance of the algorithm in respects to an increasing size of input data. There are a few rules that you should remember when calculating Big-O.
### Drop Constants
Suppose we calculate three separate for loops that add up to some `O(n) + O(n) + O(n) = O(3n)`, then we claim our runtime to be `O(n)`. This is because both `O(n)` and `O(3n)` grow at the same rate [asymptotically](https://en.wikipedia.org/wiki/Asymptotic_analysis).
### Drop Non-Dominants
Suppose that the calculation of an algorithm leaves us with Big-O `O(n) + O(n^2) + O(1)`, then we claim our runtime to be `O(n^2)`. This is because our asymptotic analysis is interested in the upper bound, and all non-dominants terms will grow slower than the dominant term.
### Extras
There are a few more (less strict) rules written on this [website](https://programmingblah.com/Big-O-Notation-Part-2/) with good examples. It is a good idea to look here if you need some more clarity regarding time complexity.

## Practice
Now that we understand how to calculate time complexity, let's take a look at a few practice problems.
1. ```py
# Determine the runtime of the following algorithm:
a = 0
for i in range(n):
    for j in range(n):
        a += 1
```
<details>
    <summary>Click here for answer</summary>
  
    There are two for loops, both will iterate `n` times. Therefore, `n` loops will iterate `n` times, giving us a Big-O of `O(n^2)`.
</details>
2. ```py
# Determine the runtime of the following algorithm:
a = 0
for i in range(1, n):
    for j in range(1, n/i):
        a += 1
```
<details>
    <summary>Click here for answer</summary>

    This one is a little trickier. If you have not taken a entry level math course at university or seen some advanced math proofs, you may struggle with this one. It uses a harmonic series, as the inner loop with iterate `n + n/2 + n/3 + ... + n/n` times, so it simplifies to `lg n`. The outer loop will iterate `n` times, giving us a total time complexity of `O(nlg n)`
</details>

## BONUS: A Unique Case
Sometimes people will write `O(n + m) = O(max(n, m))`, so why is this the case? Well, to explain let us do a quick proof as follows,
```py
# Consider the terms without Big-O notation, clearly
n + m >= max(n, m) >= (n + m) / 2
# where n and m are non-negative integers

# Therefore, we have Big-O bounds by
O(n + m) >= O(max(n, m)) >= O((n + m) / 2)

# But since we remove constants, the equation above is also equivalent to,
O(n + m) >= O(max(n ,m)) >= O(n + m)

# So in other words,
O(n + m) = O(max(n, m))
```