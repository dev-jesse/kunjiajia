```python3
from typing import (
    Set,
)

class Solution:
    """
    @param start: a string
    @param end: a string
    @param dict: a set of string
    @return: An integer
    """
    def ladder_length(self, start: str, end: str, dict: Set[str]) -> int:
        dict.add(end)
        queue = collections.deque([start])
        distance = {start: 1}

        while queue:
            word = queue.popleft()

            if word == end:
                return distance[word]

            for next_word in self.get_next_words(word, dict):
                if next_word in distance:
                    continue
                distance[next_word] = distance[word] + 1
                queue.append(next_word)

        return 0

    def get_next_words(self, word, dict):
        words = []
        for i in range(len(word)):
            prefix, suffix = word[:i], word[i + 1:]
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                next_word = prefix + ch + suffix
                if next_word not in dict:
                    continue
                words.append(next_word)
        return words
```
