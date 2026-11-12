class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tHashTable = {}
        windowHashTable = {}
        leftIndex = 0

        if len(s) < len(t):
            return ""

        for c in t:
            tHashTable[c] = tHashTable.get(c, 0) + 1
            if c not in s:
                return ""

        bestString = ""
        required = len(tHashTable)
        formed = 0

        for index, rightIndex in enumerate(s):
            if rightIndex in tHashTable:
                windowHashTable[rightIndex] = windowHashTable.get(rightIndex, 0) + 1
                # If this character's count matches the requirement in t, increment formed
                if windowHashTable[rightIndex] == tHashTable[rightIndex]:
                    formed += 1
            
            # Instant O(1) check instead of slow all() scan!
            while formed == required:
                current_window = s[leftIndex : index + 1]
                
                if bestString == "" or len(current_window) < len(bestString):
                    bestString = current_window

                # Shrink from the left
                left_char = s[leftIndex]
                if left_char in windowHashTable:
                    windowHashTable[left_char] -= 1
                    # If dropping this character breaks the requirement, decrement formed
                    if left_char in tHashTable and windowHashTable[left_char] < tHashTable[left_char]:
                        formed -= 1
                leftIndex += 1
        
        return bestString