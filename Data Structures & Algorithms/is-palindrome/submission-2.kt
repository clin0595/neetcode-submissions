class Solution {
    fun isPalindrome(s: String): Boolean {
        var filteredS = s.filter { it.isLetterOrDigit() }
    
        for (i in 0..(filteredS.length/2 - 1)) {
            println(filteredS[filteredS.length - i - 1].uppercaseChar())
            println(filteredS[i].uppercaseChar())
            if (filteredS[filteredS.length - i - 1].uppercaseChar() != filteredS[i].uppercaseChar()) {

                return false
            }
        }

        return true


    }
}
