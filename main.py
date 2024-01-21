import pygame
from Checkers.constants import *
from Checkers.game import Game
from minimax.algorithm import minimax
import time

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Monster Battle (Checkers)")

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def draw_difficulty_selection_window():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
    pygame.display.set_caption("Difficulty Selection")

    font = pygame.font.Font(None, 36)
    difficulty_options = ["Easy", "Medium", "Hard"]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        

        screen.fill((161, 83, 67))  # Crimson background color

        pygame.draw.rect(screen, (255, 255, 255), (0 + WIDTH//20, WIDTH//20, HEIGHT - HEIGHT//10 ,HEIGHT - HEIGHT//10), 5)

        text = font.render("Select Difficulty (Press on Keyboard)", True, (255, 255, 255))  # White text color
        text_rect = text.get_rect(center=(WIDTH // 2, 80))
        screen.blit(text, text_rect)

        for i, option in enumerate(difficulty_options):
            text = font.render(f"{i + 1}. {option}", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH // 2, 120 + i * 30))
            screen.blit(text, text_rect)
            screen.blit(CHOICE, (WIDTH//2 - (SQUARE_SIZE * 3), HEIGHT//2 - (SQUARE_SIZE)))

        pygame.display.flip()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            return 1  # Easy
        elif keys[pygame.K_2]:
            return 2  # Medium
        elif keys[pygame.K_3]:
            return 3  # Hard

def main():
    run = True
    clock = pygame.time.Clock()

    # Add difficulty selection
    selected_difficulty = draw_difficulty_selection_window()

    game = Game(WIN)

    while run:

        clock.tick(FPS)

        if game.turn == FUNCOLOR2:
            value, new_board = minimax(game.get_board(), selected_difficulty, FUNCOLOR2, game)
            game.ai_move(new_board)

        if game.winner() is not None:
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
                game.select(row, col)

        game.update()

    pygame.quit()

if __name__ == "__main__":
    main()
