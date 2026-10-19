class Solution {
    public boolean isAnagram(String s, String t) {

        if (s.length() != t.length()) {
            return false;
        }

        Map<String, Integer> numOfCharsMap1 = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            if (numOfCharsMap1.get(String.valueOf(s.charAt(i))) == null) {
                numOfCharsMap1.put(String.valueOf(s.charAt(i)), 1);
            } else {
                int currentNum = numOfCharsMap1.get(String.valueOf(s.charAt(i)));
                numOfCharsMap1.put(String.valueOf(s.charAt(i)), currentNum + 1);
            }
        }

        Map<String, Integer> numOfCharsMap2 = new HashMap<>();

        for (int i = 0; i < t.length(); i++) {
            if (numOfCharsMap2.get(String.valueOf(t.charAt(i))) == null) {
                numOfCharsMap2.put(String.valueOf(t.charAt(i)), 1);
            } else {
                int currentNum = numOfCharsMap2.get(String.valueOf(t.charAt(i)));
                numOfCharsMap2.put(String.valueOf(t.charAt(i)), currentNum + 1);
            }
        }

        if (numOfCharsMap1.equals(numOfCharsMap2)) {
            return true;
        } else {
            return false;
        }

    }
}
