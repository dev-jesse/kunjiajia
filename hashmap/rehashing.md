```python3
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        new_hashTable = [None] * len(hashTable) * 2
        for node in hashTable:
            while node:
                temp = node.next
                if not new_hashTable[node.val % len(new_hashTable)]:
                    new_hashTable[node.val % len(new_hashTable)] = node
                    node.next = None
                else:
                    curr = new_hashTable[node.val % len(new_hashTable)]
                    while curr.next:
                        curr = curr.next
                    curr.next = node
                    node.next = None
                node = temp
        return new_hashTable
```
