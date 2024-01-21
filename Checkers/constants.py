import pygame
import random

WIDTH = 700
HEIGHT = 700
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH//COLS

RED = (158, 27, 50)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
BLUE = (0,0,255)
GRAY = (162, 170, 173)

# Generate a random number between 0 and 255
r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
r2 = random.randint(0, 255)
g2 = random.randint(0, 255)
b2 = random.randint(0, 255)
r3 = random.randint(0, 255)
g3 = random.randint(0, 255)
b3 = random.randint(0, 255)
r4 = random.randint(0, 255)
g4 = random.randint(0, 255)
b4 = random.randint(0, 255)
hair = random.randint(2,8)

# Create a tuple of the random RGB values
FUNCOLOR = (r, g, b)
FUNCOLOR2 = (r2, g2, b2)
FUNCOLOR3 = (r3, g3, b3)
FUNCOLOR4 = (r4, g4, b4)

LIGHTBLUE = (173, 216, 230,0.5)

CROWN = pygame.image.load('assets/crown.png')
CROWN = pygame.transform.scale(CROWN, (44,25))
CAPE = pygame.image.load('assets/cape.png')
CAPE = pygame.transform.scale(CAPE, (100,60))
CAPEOVER = pygame.image.load('assets/ahh.png')
CAPEOVER = pygame.transform.scale(CAPEOVER, (75,100))
WINSCREEN = pygame.image.load('assets/winscreen.jpeg')
WINSCREEN = pygame.transform.scale(WINSCREEN, (SQUARE_SIZE * 6,SQUARE_SIZE * 4))
LOSESCREEN = pygame.image.load('assets/youlose.jpeg')
LOSESCREEN = pygame.transform.scale(LOSESCREEN, (SQUARE_SIZE * 6,SQUARE_SIZE * 4))
CHOICE = pygame.image.load('assets/choices.jpg')
CHOICE = pygame.transform.scale(CHOICE, (SQUARE_SIZE * 6,SQUARE_SIZE * 4))