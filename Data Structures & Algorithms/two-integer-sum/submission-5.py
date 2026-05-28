class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newdict = dict()
        for i, value in enumerate(nums):
            currDiff = target - value
            if currDiff in newdict:
                return [newdict[currDiff], i]
            newdict[value] = i
        return []