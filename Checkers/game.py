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
        pygame.display.update()