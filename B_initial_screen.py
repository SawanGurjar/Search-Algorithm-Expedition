from BA_curved_icon import *
from C_solver import *
from D_generator import *

color_dark = (75,75,75) 
color_white = (255,255,255) 
largefont = pygame.font.SysFont('Corbel',28)
text_easy = largefont.render('Easy' , True , color_white)
text_medium = largefont.render('Medium' , True , color_white)
text_hard = largefont.render('Hard' , True , color_white)
text_level = largefont.render('Hey! Please choose the LEVEL for sudoku Solver:' ,True ,color_dark)
text_generator_level = largefont.render('Hey! Please choose the LEVEL for sudoku Generator:' , True , color_dark)

def initial_screen(
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
        ):
    #buttons for screen
    def button(mouse):
        if 183<=mouse[0]<=483 and 200<=mouse[1]<=290:
            AAfilledRoundedRect(screen,(183, 200, 300, 90),color_light,0.8)
            AAfilledRoundedRect(screen,(183, 320, 300, 90),color_green,0.8)
            AAfilledRoundedRect(screen,(263, 635, 140, 65),color_red,0.8)
        elif 183<=mouse[0]<=483 and 320<=mouse[1]<=410:
            AAfilledRoundedRect(screen,(183, 200, 300, 90),color_blue,0.8)
            AAfilledRoundedRect(screen,(183, 320, 300, 90),color_light,0.8)
            AAfilledRoundedRect(screen,(263, 635, 140, 65),color_red,0.8)
        elif 263<=mouse[0]<=403 and 635<=mouse[1]<=700:
            AAfilledRoundedRect(screen,(183, 200, 300, 90),color_blue,0.8)
            AAfilledRoundedRect(screen,(183, 320, 300, 90),color_green,0.8)
            AAfilledRoundedRect(screen,(263, 635, 140, 65),color_red_hover,0.8)  
        else: 
            AAfilledRoundedRect(screen,(183, 200, 300, 90),color_blue,0.8)
            AAfilledRoundedRect(screen,(183, 320, 300, 90),color_green,0.8)
            AAfilledRoundedRect(screen,(263, 635, 140, 65),color_red,0.8)
    
    while True: 
        screen.fill((0,0,0))  
        screen.fill([255, 255, 255])
        screen.blit(background, ( 0,0 ))

        #stores the (x,y) coordinates into the variable as a tuple 
        mouse = pygame.mouse.get_pos()  
        button(mouse)
        #superimposing the text onto our button 
        screen.blit(text_solver, (257, 232))
        screen.blit(text_generator, (232, 352)) 
        screen.blit(text_quit, (309, 655)) 
        screen.blit(text_team, (244, 737))
          
        for ev in pygame.event.get():    
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                  
            if ev.type == pygame.MOUSEBUTTONDOWN:     
                if 263<=mouse[0]<=403 and 635<=mouse[1]<=700:
                    pygame.quit() 
                if 183<=mouse[0]<=483 and 200<=mouse[1]<=290:
                    s_solver(
                        screen, 
                        background,
                        color_white,
                        color_light,
                        color_dark,
                        color_blue, 
                        color_green,
                        color_red_hover,
                        color_red,
                        color_yellow,
                        text_level, 
                        text_easy,
                        text_medium,
                        text_hard,
                        text_quit, 
                        text_team,
                        largefont
                        )
                if 183<=mouse[0]<=483 and 320<=mouse[1]<=410:
                    generator(
                        screen,    
                        background, 
                        color_white,
                        color_light,
                        color_dark,
                        color_blue, 
                        color_green,
                        color_red_hover,
                        color_red,
                        color_yellow,
                        text_generator_level, 
                        text_easy,
                        text_medium,
                        text_hard,
                        text_quit,
                        text_team,
                        largefont
                        )
        pygame.display.update()         