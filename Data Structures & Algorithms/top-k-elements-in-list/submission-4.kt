class Solution {
    fun topKFrequent(nums: IntArray, k: Int): IntArray {
        var sortedNumCount = mutableMapOf<Int, Int>()

        for (number in nums) {
            sortedNumCount[number] = sortedNumCount.getOrDefault(number, 0) + 1
        }

        val sortedList = sortedNumCount.entries.sortedByDescending { it.value }


        val toReturn = mutableListOf<Int>()

        for (i in 0 until k) {
            toReturn.add(sortedList[i].key)
        }

        return toReturn.toIntArray()

    }

}
