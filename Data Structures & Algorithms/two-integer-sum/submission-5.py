class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {} 

        for i, n in enumerate(nums):
            index[n] = i

        for numIndex in range(len(nums)):
            needToFind = target - nums[numIndex]
            if (index.get(needToFind) != None) & (index.get(needToFind) != numIndex):
                return [numIndex, index.get(needToFind)] 
