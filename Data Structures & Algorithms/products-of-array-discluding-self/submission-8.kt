class Solution {
    fun productExceptSelf(nums: IntArray): IntArray {
        val prefixes = IntArray(nums.size)
        val suffixes = IntArray(nums.size)
        val toReturn = IntArray(nums.size)

        prefixes[0] = 1
        suffixes[(nums.size - 1)] = 1

        for (i in 1 until nums.size) {
            prefixes[i] = prefixes[i-1] * nums[i-1]
        }

        for (i in (nums.size - 2) downTo 0) {
            suffixes[i] = suffixes[i+1] * nums[i+1]
        }

        for (i in 0 until nums.size) {
            toReturn[i] = suffixes[i] * prefixes[i]
        }

        return toReturn
    }
}
