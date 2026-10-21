class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columnCheck = [{} for _ in range(9)]
        squareCheck = [{} for _ in range(9)]

        for rowIndex, row in enumerate(board):
            rowCheck = {}
            
            for entryIndex, entry in enumerate(row) :
                # obtain counts on each row
                if entry in rowCheck:
                    rowCheck[entry] = rowCheck[entry] + 1
                else :
                    rowCheck[entry] = 1

                # obtain counts on each column (column[columnIndex][entryNum])
                if entryIndex < len(columnCheck):
                    if entry in columnCheck[entryIndex]:
                        columnCheck[entryIndex][entry] = columnCheck[entryIndex][entry] + 1
                    else:
                        columnCheck[entryIndex][entry] = 1
                else :
                    columnCheck[entryIndex] = {}
                    columnCheck[entryIndex][entry] = 1

                
                # obtain counts for each square
                sqIndex = (rowIndex // 3) * 3 + (entryIndex // 3)
                if sqIndex < len(squareCheck):
                    if entry in squareCheck[sqIndex]:
                        squareCheck[sqIndex][entry] = squareCheck[sqIndex][entry] + 1
                    else:
                        squareCheck[sqIndex][entry] = 1
                else :
                    squareCheck[sqIndex] = {}
                    squareCheck[sqIndex][entry] = 1

            # check each row
            for entry in rowCheck :
                if (entry != ".") and (rowCheck[entry] > 1):
                    return False

        
        # check each column
        for column in columnCheck:
             for entry in column :
                if (entry != ".") and (column[entry] > 1):
                    return False

        # check each square
        for square in squareCheck:
             for entry in square :
                if (entry != ".") and (square[entry] > 1):
                    return False

        
        
        return True