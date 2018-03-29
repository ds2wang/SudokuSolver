class Sudoku:
    def __init__(self):
        self.board = []
    
    '''
    Enter 9 rows. use '.' to represent empty square
    '''
    def processInput(self):
        for _ in range(9):
            line = raw_input()
            row = []
            for r in range(9):
                row.append(line[r])
            self.board.append(row)
    
    def solveSudoku(self):
        board = self.board
        possibilities = [[set() for _ in range(9)] for _ in range(9)]
        rowNums = dict()
        colNums = dict()
        boxNums = dict()
        numSet = set(["1","2","3","4","5","6","7","8","9"])
        
        def initRow(row):
            rowNums[row] = set()
            for col in range(9):
                if board[row][col] != ".":
                    rowNums[row].add(board[row][col])
                    
        def initCol(col):
            colNums[col] = set()
            for row in range(9):
                if board[row][col] != ".":
                    colNums[col].add(board[row][col])
        
        def initBox(row, col):
            for i in range(row, row+3):
                for j in range(col, col+3):
                    if board[i][j] != '.':
                        boxNums[row][col].add(board[i][j])
        
        for row in range(9):
            initRow(row)
        
        for col in range(9):
            initCol(col)
        
        for row in range(0,9,3):
            boxNums[row] = dict()
            for col in range(0,9,3):
                boxNums[row][col] = set()
                initBox(row, col)
        
        def initPossibilities():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        possibilities[row][col] = numSet - (rowNums[row] | colNums[col] | boxNums[(row//3)*3][(col//3)*3])
    
        initPossibilities()
        
        def boxIsValid(row,col):
            seen = set()
            for i in range(row, row+3):
                for j in range(col, col+3):
                    if board[i][j] == '.':
                        continue
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            return True
        
        def rowIsValid(row):
            seen = set()
            for col in range(0,9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
            return True
        
        def colIsValid(col):
            seen = set()
            for row in range(0,9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in seen:
                    return False
                seen.add(board[row][col])
            return True
        
        def printBoard():
            for row in range(9):
                if row % 3 == 0:
                    print("")
                rowItems = []
                for col in range(9):
                    space = ""
                    if col % 3 == 0:
                        space = " "
                    rowItems.append(space + self.board[row][col])
                print(" ".join(rowItems))
        
        def solve():
            for row in range(9):
                for col in range(9):
                    if board[row][col] == ".":
                        for num in possibilities[row][col]:
                            board[row][col] = num
                            if rowIsValid(row) and colIsValid(col) and boxIsValid((row//3)*3,(col//3)*3) and solve():
                                return True
                        board[row][col] = "."
                        return False
            return True
        solve()
        printBoard()
        
s = Sudoku()
s.processInput()
s.solveSudoku()
                    