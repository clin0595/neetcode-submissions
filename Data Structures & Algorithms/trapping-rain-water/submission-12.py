class Solution:
    def trap(self, height: List[int]) -> int:
        toReturn = 0
        prefixMaxArray = [height[0]]

        for i in range(len(height)) :
            if i != 0 :
                if (height[i] > prefixMaxArray[i-1]) :
                    prefixMaxArray.append(height[i])
                else :
                    prefixMaxArray.append(prefixMaxArray[i-1])

        suffixMaxArray = [height[-1]]

        # second to last, stop at -1, step is -1 (count backwards)
        for i in range(len(height) - 2, -1, -1):
            if (height[i] > suffixMaxArray[-1]) :
                suffixMaxArray.append(height[i])
            else :
                suffixMaxArray.append(suffixMaxArray[-1])

        # Flip it back so it aligns with left-to-right indices
        suffixMaxArray.reverse()

        for i in range(len(height)) :
            toReturn = toReturn + min(prefixMaxArray[i], suffixMaxArray[i]) - height[i]

        return toReturn


            