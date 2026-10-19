class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sortedNumsCount = {}

        for number in nums:
            if number in sortedNumsCount:
                sortedNumsCount[number] = sortedNumsCount[number] + 1
            else:
                sortedNumsCount[number] = 1

        sortedList = sorted(sortedNumsCount.items(), key=lambda item: item[1], reverse=True)
        
        toReturn = []

        for i in range(k):
            toReturn.append(sortedList[i][0])

        return toReturn



