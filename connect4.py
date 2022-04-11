import numpy as np 
import pygame
import sys
import math

BLUE = (0,0,255)
BLACK  = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
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

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen,BLUE,(c*SQUARESIZE,r*SQUARESIZE+SQUARESIZE,SQUARESIZE,SQUARESIZE))
            pygame.draw.circle(screen,BLACK,(int(c*SQUARESIZE+SQUARESIZE/2),int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)),RADIUS)
            
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            # check if player 1 Red
            if board[r][c] == 1:
                pygame.draw.circle(screen,RED,(int(c*SQUARESIZE+SQUARESIZE/2),height - int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen,GREEN,(int(c*SQUARESIZE+SQUARESIZE/2),height - int(r*SQUARESIZE+SQUARESIZE/2)),RADIUS)
    # take note: you need to update if you are something to manipulate in the window
    pygame.display.update()

board = create_board()

print_board(board)
game_over =  False
# check if player 1 turn or player 2 
turn = 0

# initialize the pygame  
pygame.init()

# how big the board is
SQUARESIZE = 100
width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT + 1) * SQUARESIZE

# put width and height inside the tuple
size = (width,height)
# get the radius
RADIUS = int(SQUARESIZE/2 - 5)

# generate the size of the screen
screen = pygame.display.set_mode(size=size)
draw_board(board=board)
#  if you want to change any design you need to update after
pygame.display.update()

# initializing the font
myFont = pygame.font.SysFont("monospace",75)
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             exit(1)

while not game_over:

    # to open pygame window you need this
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(1)
        # this function purpose is track the movement of the mouse
        if event.type == pygame.MOUSEMOTION:
            posX = event.pos[0]
            pygame.draw.rect(screen,BLACK,(0,0,width,SQUARESIZE))
            if turn == 0 :
                pygame.draw.circle(screen,RED,(posX,SQUARESIZE/2),RADIUS)
            else :
                pygame.draw.circle(screen,GREEN,(posX,SQUARESIZE/2),RADIUS)
            pygame.display.update()

        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen,BLACK,(0,0,width,SQUARESIZE))

            # print(event.pos)
            if turn == 0 :
            # Player 1 
                #  get the position of  x axis
                posX = event.pos[0]
                # col = int(input("Player 1 Make your Selection (0-6) :"))
                col = int(math.floor(posX/SQUARESIZE))
                print(col)
                turn = 1

                if is_valid_location(board=board,col=col):
                    row = get_next_open_row(board=board,col=col)
                    drop_piece(board=board, row=row,col=col,piece=1)

                    # check if player 1 won 
                    if winning_move(board=board,piece=1):
                        print("Congrats Player 1 Won")
                        label = myFont.render("Player 1 Won",1,RED)
                        screen.blit(label,(40,10))
                        game_over = True
                else:
                    turn = 0
               
            else:
                    # Player 2  
                posX = event.pos[0]
                # col = int(input("Player 2 Make your Selection (0-6) :"))
                col = int(math.floor(posX/SQUARESIZE))
                turn = 0

                if is_valid_location(board=board,col=col):
                    row = get_next_open_row(board=board,col=col)
                    drop_piece(board=board, row=row,col=col,piece=2)
                    # check if player 2 won 
                    if winning_move(board=board,piece=2):
                        # print("Congrats Player 2 Won")
                        label = myFont.render("Player 2 Won",1,GREEN)
                        screen.blit(label,(40,10))
                        game_over = True
                else:
                    turn = 0
            print_board(board)
            draw_board(board=board)
                # turn+= 1
                # turn%=2
            
            # check if the game is over
            if game_over :
                pygame.time.wait(3000)