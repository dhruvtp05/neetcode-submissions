class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
           bit = (n >> i) & 1

           placed = bit << (31 - i) 

           result = result | placed

        return result