# Katelyn Curtiss
# 3-17-25

import pygame 
import sys 
import config

def draw_text(screen,text, x,y,font_size, color, font_name=None, bold=False, italic=False):
    if font_name:
        font = pygame.font.Font(font_name, font_size)
    else:
        font = pygame.font.Font(None, font_size)
    font.set_bold(bold)
    font.set_italic(italic)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x,y)) 

    def init_game 