class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check unique rows
        for row in board:
            memoryRows=set()
            for element in row:
                if element != "." and element in memoryRows:
                    return False
                memoryRows.add(element)
        
        for column in range(len(board[0])):
            memoryColumns=set()
            for row in range(len(board)):
                element = board[row][column]
                if element!= "." and element in memoryColumns:
                    return False
                memoryColumns.add(element)

        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                seen=set()
                for i in range(3):
                    for j in range(3):
                        element=board[box_row+i][box_col+j]
                        if element!="." and element in seen:
                            return False
                        seen.add(element)
        return True
        
