class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        correct = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        correct = [i, j]
                        return correct
