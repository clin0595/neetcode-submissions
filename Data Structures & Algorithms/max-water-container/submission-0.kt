class Solution {
    fun maxArea(heights: IntArray): Int {
        var biggestVolume = 0

        var i = 0
        var j = heights.size - 1
        while (i < j) {
            val vol = ((j-i)*min(heights[i],heights[j]))
            if (biggestVolume < vol) {
                biggestVolume = vol
            }
            if ((i+1 < j) && heights[i] < heights[j]) {
                i++
            } else {
                j--
            }
            
        }
        return biggestVolume


    }
}
