class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key is index and value is value at that index
        diffs = {}

        for i, v in enumerate(nums):
            difference = target - nums[i]

            if difference in diffs:
                return [diffs[difference], i]

            diffs[v] = i
        return []