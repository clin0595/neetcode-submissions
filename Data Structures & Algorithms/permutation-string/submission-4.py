class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count = dict()
        currentStrProgress = dict()
        i = 0

        for c in s1 :
            s1Count[c] = s1Count.get(c,0) + 1

        for j in range(len(s2)) :
            print("s2[i]: "+s2[i])
            print("s2[j]: "+s2[j])

            print(s1Count)
            print(currentStrProgress)
            if s2[j] in s1Count:
                currentStrProgress[s2[j]] = currentStrProgress.get(s2[j], 0) + 1

                while currentStrProgress[s2[j]] > s1Count[s2[j]]:
                    currentStrProgress[s2[i]] -= 1
                    i += 1
            else :
                currentStrProgress.clear()
                i = j + 1

            if s1Count == currentStrProgress :
                return True


        return False
            