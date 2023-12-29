# Controls the game mech, whose turn, did you select a piece, can you move here, handles drawing everything like moves.
import pygame
from Checkers.board import Board
from .constants import *

class Game:
    def __init__(self, win):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.win = win

    def update(self):
        self.board.draw_board(self.win)
        self.draw_jumpable_spaces(self.valid_moves)
        pygame.display.update()

    
    def reset(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def select(self, row, col):
        if self.selected:
            # if we have already selected something, lets try to move what we have selectee to the row and column we put it in
            result = self._move_game_piece(row,col)
            if not result:
                self.selected = None
                self.select(row,col)
        else:
            piece = self.board.get_piece(row, col)
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self. valid_moves = self.board.get_valid_moves(piece)
                return True
        return False

    def _move_game_piece(self, row, col):
        piece = self.board.get_piece(row,col)
        if self.selected and piece == 0 and (row,col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            self.change_turn()
        else:
            return False
        return True
    
    # Inverses the color which is currently able to move
    def change_turn(self):
        if self.turn == RED:
            self.turn == WHITE
        else:
            self.turn == RED

    def draw_jumpable_spaces(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.rect(self.win,LIGHTBLUE,(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))