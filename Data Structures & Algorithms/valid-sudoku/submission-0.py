class Solution:
    def checkSubBox(self, board:List[List[str]], row: int, col: int) -> bool:
        arr_sub = []
        for i in range(row, row + 3):
            for j in range(col, col + 3):
                if board[i][j] != ".":
                    arr_sub.append(int(board[i][j]))

            if (len(arr_sub) != len(set(arr_sub))):
                return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            arr_hor = []
            arr_ver = []
            for j in range(9):
                if board[i][j] != ".":
                    arr_hor.append(int(board[i][j]))

            if (len(arr_hor) != len(set(arr_hor))):
                return False

            for k in range(9):
                if board[k][i] != ".":
                    arr_ver.append(int(board[k][i]))

                if (len(arr_ver) != len(set(arr_ver))):
                    return False

        for l in range(0, 7, 3):
            for m in range(0, 7, 3):
                value = self.checkSubBox(board, l, m)
                if not value:
                    return False

        return True
        