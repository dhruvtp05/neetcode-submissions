class Solution:
    def hammingWeight(self, n: int) -> int:
        r = 32
        amount = 0

        for i in range(r):
            if (1 << i) & n:
                amount += 1
        return amount

