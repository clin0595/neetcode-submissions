class Solution {
    fun isValidSudoku(board: Array<CharArray>): Boolean {
        val columnCheck = Array(9) { mutableMapOf<Char, Int>() }
        val squareCheck = Array(9) { mutableMapOf<Char, Int>() }

        for ((rowIndex, row) in board.withIndex()) {
            val rowCheck = mutableMapOf<Char, Int>()
            
            for ((entryIndex, entry) in row.withIndex()) {
                // 1. Obtain counts on each row
                rowCheck[entry] = rowCheck.getOrDefault(entry, 0) + 1

                // 2. Obtain counts on each column
                if (entryIndex < columnCheck.size) {
                    columnCheck[entryIndex][entry] = columnCheck[entryIndex].getOrDefault(entry, 0) + 1
                } else {
                    columnCheck[entryIndex] = mutableMapOf(entry to 1)
                }

                // 3. Obtain counts for each square
                val sqIndex = (rowIndex / 3) * 3 + (entryIndex / 3)
                if (sqIndex < squareCheck.size) {
                    squareCheck[sqIndex][entry] = squareCheck[sqIndex].getOrDefault(entry, 0) + 1
                } else {
                    squareCheck[sqIndex] = mutableMapOf(entry to 1)
                }
            }

            // Check each row
            for ((entry, count) in rowCheck) {
                if (entry != '.' && count > 1) {
                    return false
                }
            }
        }

        // Check each column
        for (column in columnCheck) {
            for ((entry, count) in column) {
                if (entry != '.' && count > 1) {
                    return false
                }
            }
        }

        // Check each square
        for (square in squareCheck) {
            for ((entry, count) in square) {
                if (entry != '.' && count > 1) {
                    return false
                }
            }
        }

        return true
    }
}