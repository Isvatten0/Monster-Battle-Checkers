import pygame
from .constants import *
import math

class Piece:
    PADDING = 20
    BORDER = 2

    # Initialize attributes
    def __init__(self, row, col, color):
        # set pulled in values
        self.row = row
        self.col = col
        self.color = color

        # default piece is a non king
        self.king = False

        self.x = 0
        self.y = 0
        self.calc_postion()

    # calculate the postion of the piece on the board, in its own seperate function as this will be called many times other than the start.
    def calc_postion(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    # draw the game piece and the border around it. The boarder is just a bigger off color circle underneath.
    def draw_piece(self, win):
        
        radius = SQUARE_SIZE // 2 - self.PADDING

        if self.king:
            win.blit(CAPE, (self.x - CAPE.get_width()//2, self.y + CAPE.get_height()//7))
        else:
            # Draw triangle hair around the top of the circle
            hair_length = 20
            num_triangles = hair
            if self.color == FUNCOLOR:
                hair_color = FUNCOLOR3  
            else:
                hair_color = FUNCOLOR4 

            for i in range(num_triangles):
                angle = math.radians(i * (360 / num_triangles))
                x1 = self.x + int(radius * math.cos(angle))
                y1 = self.y + int(radius * math.sin(angle))
                x2 = self.x + int((radius + hair_length) * math.cos(angle))
                y2 = self.y + int((radius + hair_length) * math.sin(angle))
                x3 = self.x + int((radius + hair_length) * math.cos(math.radians(i * (360 / num_triangles) + 180 / num_triangles)))
                y3 = self.y + int((radius + hair_length) * math.sin(math.radians(i * (360 / num_triangles) + 180 / num_triangles)))
                pygame.draw.polygon(win, hair_color, [(x1, y1), (x2, y2), (x3, y3)])

        # Draw main Piece
        pygame.draw.circle(win, GRAY, (self.x, self.y), radius + self.BORDER)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)

        # Draw eyes
        eye_radius = 5
        left_eye_position = (self.x - radius // 2, self.y - radius // 4)
        right_eye_position = (self.x + radius // 2, self.y - radius // 4)
        pygame.draw.circle(win, (0, 0, 0), left_eye_position, eye_radius)
        pygame.draw.circle(win, (0, 0, 0), right_eye_position, eye_radius)

        # Draw mouth (a simple arc for a smile)
        mouth_radius = radius // 2
        start_angle = 0  # start angle of the arc
        end_angle = 180  # end angle of the arc
        mouth_rect = (self.x - mouth_radius, self.y, 2 * mouth_radius, mouth_radius)
        pygame.draw.arc(win, (0, 0, 0), mouth_rect, start_angle, end_angle, 2)

        # Draw golden tooth rectangle inside the mouth
        tooth_width = 4
        tooth_height = 5
        tooth_position = (self.x + 4 - tooth_width // 2, self.y + 7 - tooth_height // 2)
        pygame.draw.rect(win, (255, 215, 0), (tooth_position[0], tooth_position[1], tooth_width, tooth_height))

        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - 2 * CROWN.get_height()//1))
            
    def move_update_position(self, row, col):
        self.row = row
        self.col = col
        self.calc_postion()

    # what is the internal representation of this object. Used for debugginging.    
    def __repr__(self):
        return str(self.color)
    