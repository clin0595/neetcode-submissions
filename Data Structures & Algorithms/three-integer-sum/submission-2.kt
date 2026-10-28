class Solution {
    fun threeSum(nums: IntArray): List<List<Int>> {
        var toReturn = mutableListOf<List<Int>>()
        nums.sort()

        for (i in 0 until nums.size - 2) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue
            }
            var k = nums.size - 1
            var j = i + 1
            while (j < k) {
                if (nums[i] + nums[j] + nums[k] == 0) {
                    val toAdd = mutableListOf<Int>(nums[i], nums[j], nums[k])
                    toReturn.add(toAdd)
                    
                    while (j < k && nums[j+1] == nums[j]) {
                        j++
                    }
                    j++
                    
                    while (k > j && nums[k-1] == nums[k]) {
                        k--
                    }
                    k--


                } else if (nums[i] + nums[j] + nums[k] < 0) {
                    j++
                } else {
                    k--
                }
            
            }
        }
        return toReturn
    }
}
