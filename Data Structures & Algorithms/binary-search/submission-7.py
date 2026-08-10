class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1

        while left <= right:
            # Midway Calculation
            midway = left + ((right - left) // 2)

            # Has to be on the left
            if nums[midway] > target:
                right = midway - 1

            # Has to be on the right
            elif nums[midway] < target:
                left = midway + 1

            # Number found
            else: 
                return midway
        return -1
