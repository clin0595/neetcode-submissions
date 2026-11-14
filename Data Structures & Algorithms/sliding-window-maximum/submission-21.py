class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        windowValuesTable = {}
        
        maxList = []
        leftIndex = 0

        for i in range(k) :
            windowValuesTable[nums[i]] = windowValuesTable.get(nums[i], 0) + 1

        maxInWindow = max(windowValuesTable)

        if k == len(nums) :
            print("k == length of nums")
            return [max(nums)]

        rightIndex = k-1
        while rightIndex < len(nums) :

            if leftIndex != 0 :
                windowValuesTable[nums[rightIndex]] = windowValuesTable.get(nums[rightIndex], 0) + 1
                windowValuesTable[nums[leftIndex - 1]] = windowValuesTable.get(nums[leftIndex - 1], 0) - 1
                if windowValuesTable.get(nums[leftIndex - 1]) <= 0 :
                    windowValuesTable.pop(nums[leftIndex - 1])
            # print(windowValuesTable)
            
            if maxInWindow in windowValuesTable :
                if maxInWindow < nums[rightIndex]:
                    maxInWindow = nums[rightIndex]
            else :
                maxInWindow = max(windowValuesTable)
                
            
            maxList.append(maxInWindow)
            # print(maxInWindow)
            leftIndex += 1
            rightIndex += 1

        return maxList
