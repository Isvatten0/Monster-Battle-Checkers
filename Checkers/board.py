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

    def get_jumpable_spaces(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row
        if piece.color == RED or piece.king:
            # moves.update(self._traverse_left(
            # row - 1, Looks upward since it is RED
            # max(row-3,-1), HOW many rows up am I looking up in this case 2 rows higher
            # -1, piece.color, color
            # left)) WHere we are starting
            moves.update(self._traverse_left(row - 1, max(row-3,-1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row-3,-1), -1, piece.color, right))
            
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row + 1, min(row+3,ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, max(row+3,ROWS), 1, piece.color, right))

        return moves

    # step says if we are going up or down
    def _traverse_left(self, start, stop, stepsize, color, left, skipped=[]):
        moves = {}
        last = []
        for rows in range(start, stop, stepsize):
            if left < 0:
                break

            current = self.board[rows][left]
            if current == 0: #if we fouhd an empty square
                if skipped and not last: # we found a blank square but we cant move there
                    break
                elif skipped:
                    moves[(rows,left)] = last + skipped # where we are double jumping
                else:
                    moves[(rows,left)] = last # add as possible move 

                if last: # and last had a value in it, we found something when looping
                    if stepsize == -1:
                        row= max(rows-3,0)
                    else:
                        row= min(rows+3,ROWS)

                    moves.update(self._traverse_left(rows+stepsize,rows, stepsize,color,left-1,skipped=last))
                    moves.update(self._traverse_right(rows+stepsize,rows, stepsize,color,left+1,skipped=last))
                    break
            elif current.color == color: # otherwise if there is a piece with a color and its our same color, then we cannot move there
                break
            else: # otherwise, we could jump over it if it is a empty square next
                last = current

            left -= 1
        return moves

    def _traverse_right(self, start, stop, stepsize, color, right, skipped=[]):
        moves = {}
        last = []
        for rows in range(start, stop, stepsize):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0: #if we fouhd an empty square
                if skipped and not last: # we found a blank square but we cant move there
                    break
                elif skipped:
                    moves[(rows,right)] = last + skipped # where we are double jumping
                else:
                    moves[(rows,right)] = last # add as possible move 

                if last: # and last had a value in it, we found something when looping
                    if stepsize == -1:
                        row= max(rows-3,0)
                    else:
                        row= min(rows+3,ROWS)

                    moves.update(self._traverse_left(rows+stepsize,rows, stepsize,color,right-1,skipped=last))
                    moves.update(self._traverse_right(rows+stepsize,rows, stepsize,color,right+1,skipped=last))
                    break
            elif current.color == color: # otherwise if there is a piece with a color and its our same color, then we cannot move there
                break
            else: # otherwise, we could jump over it if it is a empty square next
                last = current

            right += 1

        return moves