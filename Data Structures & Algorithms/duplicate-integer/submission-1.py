class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newdict = dict()
        for i in nums:
            if i in newdict:
                return True
            else:
                newdict[i] = True
        return False
        