class Solution {
    public boolean hasDuplicate(int[] nums) {
        int[] sortedList = Arrays.copyOf(nums, nums.length);
        Arrays.sort(sortedList);

        for (int i = 1; i < nums.length; i++) {
            if (sortedList[i-1] == sortedList[i]) {
                return true;
            } 
        }
        return false;
    }
}