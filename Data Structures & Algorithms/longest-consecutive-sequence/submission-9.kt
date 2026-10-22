class Solution {
    fun longestConsecutive(nums: IntArray): Int {
        var numsHashset = nums.toHashSet()
        var toReturn = 0

        for (n in numsHashset) {
            var currentNum = n
            var currentStreak = 1

            if (!numsHashset.contains(n-1)) {
                while (currentNum + 1 in numsHashset) {
                    currentStreak++
                    currentNum++
                }
            }
            if (currentStreak > toReturn) {
                toReturn = currentStreak
            }
        }

        return toReturn
    }
}
