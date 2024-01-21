import pygame
from Checkers.constants import *
from Checkers.game import Game
from minimax.algorithm import minimax
import time

FPS = 60
WIN = pygame.display.set_mode((WIDTH,HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Monster Battle (Checkers)")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        
        clock.tick(FPS)

        if game.turn == FUNCOLOR2:
            value, new_board = minimax(game.get_board(), 1, FUNCOLOR2, game)
            game.ai_move(new_board)

        if game.winner() != None:
            if FUNCOLOR2 == game.winner():
                name = "The AI Wins! :()"
                WIN.blit(LOSESCREEN, (SQUARE_SIZE, SQUARE_SIZE * 2))
                pygame.display.update()
                time.sleep(2)
            else:
                name = "You Won! :)"
                WIN.blit(WINSCREEN, (SQUARE_SIZE, SQUARE_SIZE * 2))
                pygame.display.update()
                time.sleep(2)
            print(name)
            run = False
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row,col)

        game.update()

    pygame.quit()
main()