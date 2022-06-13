```python3
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        queue = deque([beginWord])
        distance = {beginWord: 1}
        
        while queue:
            word = queue.popleft()
            
            if word == endWord:
                return distance[word]
            
            for next_word in self.get_next_words(word, wordList):
                if next_word in distance:
                    continue
                queue.append(next_word)
                distance[next_word] = distance[word] + 1
                
        return 0
                
    def get_next_words(self, word, wordList):
        words = []
        for i in range(len(word)):
            left, right = word[:i], word[i + 1:]
            for char in 'abcdefghijklmnopqrstuvwxyz':
                next_word = left + char + right
                if next_word in wordList:
                    words.append(next_word)
        
        return words
```
