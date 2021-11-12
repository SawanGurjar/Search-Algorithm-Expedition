import pygame 

pygame.init() 
screen = pygame.display.set_mode((666,800))

#pygame window caption and icon
pygame.display.set_caption("Team Valorant's SUDOKU")
icon=pygame.image.load("media/icon.png")
pygame.display.set_icon(icon)
background = pygame.image.load('media/background.jpg')

#pygame background sound
#pygame.mixer.music.load(r'media/ring.mp3')
#pygame.mixer.music.set_volume(0.1)
#pygame.mixer.music.play(-1)
 
#colours
color_dark = (75,75,75)
color_white = (255,255,255)
color_light = (170,170,170)
color_red_hover = (184,15,10)

color_red = (255, 62, 48)
color_green = (23, 156, 82)
color_blue = (23, 107, 239)
color_yellow = (247, 181, 41)

#defining a font 
largefont = pygame.font.SysFont('Corbel',28)
smallfont = pygame.font.SysFont('Corbel',15)
text_quit = largefont.render('Quit' , True , color_white)
text_team = smallfont.render('the TEAM  VALORANT project', True, color_dark)

text_solver = largefont.render('Sudoku Solver' , True , color_white)
text_generator = largefont.render('Sudoku Generator' , True , color_white)

#import files
from B_initial_screen import *
initial_screen(
    screen, 
    background, 
    color_light,
    color_blue, 
    color_green,
    color_red_hover,
    color_red,
    color_yellow,
    text_solver, 
    text_generator, 
    text_quit, 
    text_team
    )


#include timer