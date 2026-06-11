# https://neetcode.io/problems/valid-sudoku/question?list=neetcode150
from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = [[] for _ in range(n)]
        columns = [[] for _ in range(n)]
        boxes = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue

                val = board[i][j]
                box_index = (i // 3) * 3 + (j // 3)

                if val in rows[i]:
                    return False
                rows[i].append(val)

                if val in columns[j]:
                    return False
                columns[j].append(val)

                if val in boxes[box_index]:
                    return False
                boxes[box_index].append(val)

        return True
s = Solution()
print(s.isValidSudoku([["1","2",".",".","3",".",".",".","."],["4",".",".","5",".",".",".",".","."],[".","9","8",".",".",".",".",".","3"],["5",".",".",".","6",".",".",".","4"],[".",".",".","8",".","3",".",".","5"],["7",".",".",".","2",".",".",".","6"],[".",".",".",".",".",".","2",".","."],[".",".",".","4","1","9",".",".","8"],[".",".",".",".","8",".",".","7","9"]]))
board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
print(s.isValidSudoku(board))
