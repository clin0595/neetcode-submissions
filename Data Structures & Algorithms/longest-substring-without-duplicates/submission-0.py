class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        checkForRepeats = set()
        longestSubstringLength = 0
        leftPointer = 0

        for rightPointer in range(len(s)) :
            while s[rightPointer] in checkForRepeats:
                checkForRepeats.remove(s[leftPointer])
                leftPointer += 1
           
            checkForRepeats.add(s[rightPointer])
            if longestSubstringLength < rightPointer - leftPointer + 1 :
                longestSubstringLength = rightPointer - leftPointer + 1

        return longestSubstringLength
