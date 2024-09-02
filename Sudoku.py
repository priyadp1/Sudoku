def validBox(board, row, column, number):
  startRow = (row // 3) * 3
  startCol = (column // 3) * 3
  for r in range(startRow, startRow + 3):
        for c in range(startCol, startCol + 3):
            if board[r][c] == number:
                return False
  return True
def validRow(board, row, number):
    return number not in board[row]
def validColumn(board, column, number):
    for r in range(9):
        if board[r] [column] == number:
            return False
    return True
def validMove(board, row, column, number):
    return(validColumn(board, column, number) and validBox(board, row, column, number) and validRow(board, row, number))
def createMiniBoard():
    board = [
    [5, 3, '*', '*', 7, '*', '*', '*', '*'],
    [6, '*', '*', 1, 9, 5, '*', '*', '*'],
    ['*', 9, 8, '*', '*', '*', '*', 6, '*'],
    [8, '*', '*', '*', 6, '*', '*', '*', 3],
    [4, '*', '*', 8, '*', 3, '*', '*', 1],
    [7, '*', '*', '*', 2, '*', '*', '*', 6],
    ['*', 6, '*', '*', '*', '*', 2, 8, '*'],
    ['*', '*', '*', 4, 1, 9, '*', '*', 5],
    ['*', '*', '*', '*', 8, '*', '*', 7, 9]
]
    return board
def printBoard(board):
    for row in board:
        print(row)
def findEmptyCell(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == '*':
                return r, c
    return None, None
def solveSudoku(board):
    row , column = findEmptyCell(board)
    if row is None:
        return True
    for number in range(1,10):
        if validMove(board, row, column, number):
            board[row][column] = number
            if solveSudoku(board):
                return True
            board[row][column] = '*'
    return False

def main():
  board = createMiniBoard()
  print("Initial Board: ")
  printBoard(board)
  if solveSudoku(board):
      print("\nSolution: ")
      printBoard(board)
  else:
      print("No solution exists for this board")
if __name__ == "__main__":
    main()