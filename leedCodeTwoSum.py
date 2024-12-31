class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDictionary = {}
        for i in range(len(nums)):
            if target - nums[i] in numDictionary:
                return [numDictionary[target - nums[i]], i]
            else:
                numDictionary[nums[i]] = i