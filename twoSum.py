### Two Sum - Completed July 2nd, 2024
## Runtime of 3801 ms beats 5%
## Memory of 17.29 MB beats 91.29%

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        correct = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        correct = [i, j]
                        return correct
