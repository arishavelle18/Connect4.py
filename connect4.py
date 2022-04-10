from enum import Flag
from pickle import TRUE
import numpy as np 

ROW_COUNT = 6
COLUMN_COUNT = 7

# initializing create_board():
def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board, row, col , piece):
    board[row][col] = piece
    pass

# check if is valid to insert or not 
def is_valid_location(board,col):
    return board[ROW_COUNT-1][col] == 0

# just checking if the element is equal to zero then it will use it to manipulate to drop a piece 
def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    # when you flip it the array of element is decreasing 
    print(np.flip(board,0))
    
def winning_move(board,piece):
    # check horizontal if you won
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # check for vertizal
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True
    
    # check positive slope for diagonal
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # check negative slope for diagonal
    for c in range(COLUMN_COUNT-3):
        for r in range(3,ROW_COUNT):
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True


board = create_board()

print_board(board)
game_over =  False
# check if player 1 turn or player 2 
turn = 0

while not game_over:

    if turn == 0 :
        # Player 1 
        col = int(input("Player 1 Make your Selection (0-6) :"))
        turn = 1

        if is_valid_location(board=board,col=col):
            row = get_next_open_row(board=board,col=col)
            drop_piece(board=board, row=row,col=col,piece=1)

            # check if player 1 won 
            if winning_move(board=board,piece=1):
                print("Congrats Player 1 Won")
                game_over = TRUE
    else:
        # Player 2  
        col = int(input("Player 2 Make your Selection (0-6) :"))
        turn = 0

        if is_valid_location(board=board,col=col):
            row = get_next_open_row(board=board,col=col)
            drop_piece(board=board, row=row,col=col,piece=2)
            # check if player 2 won 
            if winning_move(board=board,piece=2):
                print("Congrats Player 2 Won")
                game_over = TRUE
    print_board(board)
    # turn+= 1
    # turn%=2