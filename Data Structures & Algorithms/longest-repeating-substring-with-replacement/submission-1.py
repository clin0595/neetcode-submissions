class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashTable = {}
        leftPointer = 0
        longestStr = 0
        maxFreq = 0

        for rightPointer in range(len(s)) :
            hashTable[s[rightPointer]] = hashTable.get(s[rightPointer], 0) + 1
            maxFreq = max(maxFreq, hashTable[s[rightPointer]])

            if (rightPointer - leftPointer + 1) - maxFreq > k:
                hashTable[s[leftPointer]] -= 1
                leftPointer += 1

            longestStr = max(longestStr, rightPointer - leftPointer + 1)
        return longestStr

            
