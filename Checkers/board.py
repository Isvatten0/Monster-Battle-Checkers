import pygame
from .constants import *
from .piece import *

class Board:
    def __init__(self):
        self.board = []
        self.red_left = 12
        self.white_left = 12
        self.red_kings = 0
        self.white_kings = 0
        self.create_board()
    
    def draw_squares(self, win):
        # Fill the entire window with a black background
        win.fill(BLACK)

        # Fill the rows with a respective background
        for row in range(ROWS):
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(win, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else:
                    pygame.draw.rect(win, BLACK, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def get_piece(self, row, col):
        return self.board[row][col]

    def move(self, piece, row, col):
        # delete piece
        # change piece positon
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move_update_position(row, col)
        if row == ROWS or row == 0:
            piece.make_king()
            if piece.color == RED:
                self.red_kings = self.red_kings + 1
            else:
                self.white_kings = self.white_kings + 1
    
    def create_board(self):
        for row in range(ROWS):
            # we want to ahve a list that represents what each row has inside of it.
            self.board.append([])

            # add piece or empty space based on if it should be there, essentially creating a matrix
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row,col,FUNCOLOR2))
                    elif row > 4:
                        self.board[row].append(Piece(row,col,FUNCOLOR))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    # draws all the pieces and the squares
    def draw_board(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw_piece(win)