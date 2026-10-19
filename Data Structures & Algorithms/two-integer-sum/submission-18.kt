class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        var index = mutableMapOf<Int,Int>()

        for ((i,n) in nums.withIndex()) {
            index[n] = i
        }

        for ((i,n) in nums.withIndex()) {
            var needToFind = target - n
            if ((index[needToFind] != i) && (index[needToFind] != null)) {
                return intArrayOf(i, index[needToFind]!!)
            }
        }
        return intArrayOf()
    }
}
