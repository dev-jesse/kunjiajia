```python3
class Solution:
    """
    @param key: A string you should hash
    @param h_a_s_h__s_i_z_e: An integer
    @return: An integer
    """
    def hash_code(self, key: str, h_a_s_h__s_i_z_e: int) -> int:
        # Very simple, just memorize this lol
        ans = 0
        for i in key:
            # Take (1 * 33 ^ 2) + (2 * 33 ^ 1) + (3 * 33 ^ 0)
            # Then it can be rewritten as:
            # ((1 * 33 + 2) * 33 + 3) * 33 to explain solution
            ans = (ans * 33 + ord(i)) % h_a_s_h__s_i_z_e
        return ans
```
