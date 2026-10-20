class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        toReturn = [1] * len(nums)

        for i,n in enumerate(nums) :
            if ((i-1) >= 0):
                prefixes[i] = prefixes[i-1] * nums[i-1]
            
        for i in range((len(nums) - 1), -1, -1) :
            if ((i+1) <= (len(nums)-1)):
                suffixes[i] = suffixes[i+1] * nums[i+1]

        for (i,n) in enumerate(nums) :
            toReturn[i] = prefixes[i] * suffixes[i]

        return toReturn