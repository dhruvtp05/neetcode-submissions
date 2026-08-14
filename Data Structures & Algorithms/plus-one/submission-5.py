class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        new = list(digits)

        for i in range(len(digits)-1,-1,-1):
            if new[i] < 9:
                new[i] += 1
                return new
            else:
                new[i] = 0
        new.insert(0, 1)
        return new
            