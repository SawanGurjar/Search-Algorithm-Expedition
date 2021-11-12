from BA_curved_icon import *
from DA_blank_grid import *
#from DAA_algo_generator import *

def generator(
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
        ):
    
    add_line = 65
    position = [14, 84, 153, 232, 302, 371, 448, 518, 587]
    text_home = largefont.render('Home' , True , color_white)
    
    #buttons for screen
    def button(mouse):
        if 183<=mouse[0]<=483 and 200<=mouse[1]<=290:
            AAfilledRoundedRect(screen,(183, 200, 300, 90),color_light,0.8)
            AAfilledRoundedRect(screen,(183, 320, 300, 90),color_yellow,0.8)
            AAfilledRoundedRect(screen,(183, 440, 300, 90),color_green,0.8)
            AAfilledRoundedRect(screen,(263, 635, 140, 65),color_red,0.8)
        elif 183<=mouse[0]<=483 and 320<=mouse[1]<=410:
            AAfilledRoundedRect(screen,(183, 200, 300, 90),color_blue,0.8)
            AAfilledRoundedRect(screen,(183, 320, 300, 90),color_light,0.8)
            AAfilledRoundedRect(screen,(183, 440, 300, 90),color_green,0.8)
            AAfilledRoundedRect(screen,(263, 635, 140, 65),color_red,0.8)
        elif 183<=mouse[0]<=483 and 440<=mouse[1]<=530:
            AAfilledRoundedRect(screen,(183, 200, 300, 90),color_blue,0.8)
            AAfilledRoundedRect(screen,(183, 320, 300, 90),color_yellow,0.8)
            AAfilledRoundedRect(screen,(183, 440, 300, 90),color_light,0.8)
            AAfilledRoundedRect(screen,(263, 635, 140, 65),color_red,0.8)
        elif 263<=mouse[0]<=403 and 635<=mouse[1]<=700:
            AAfilledRoundedRect(screen,(183, 200, 300, 90),color_blue,0.8)
            AAfilledRoundedRect(screen,(183, 320, 300, 90),color_yellow,0.8)
            AAfilledRoundedRect(screen,(183, 440, 300, 90),color_green,0.8)
            AAfilledRoundedRect(screen,(263, 635, 140, 65),color_red_hover,0.8)  
        else: 
            AAfilledRoundedRect(screen,(183, 200, 300, 90),color_blue,0.8)
            AAfilledRoundedRect(screen,(183, 320, 300, 90),color_yellow,0.8)
            AAfilledRoundedRect(screen,(183, 440, 300, 90),color_green,0.8)
            AAfilledRoundedRect(screen,(263, 635, 140, 65),color_red,0.8)
    
    while True: 
        screen.fill((0,0,0))  
        screen.fill([255, 255, 255])
        screen.blit(background, ( 0,0 ))

        #stores the (x,y) coordinates into the variable as a tuple 
        mouse = pygame.mouse.get_pos()  
        button(mouse)
        #superimposing the text onto our button 
        screen.blit(text_generator_level, (47, 150))
        screen.blit(text_easy, (305, 232))
        screen.blit(text_medium, (290, 352)) 
        screen.blit(text_hard, (303, 472)) 
        screen.blit(text_quit, (309, 655)) 
        screen.blit(text_team, (244, 737))
          
        for ev in pygame.event.get():    
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                  
            if ev.type == pygame.MOUSEBUTTONDOWN:     
                if 263<=mouse[0]<=403 and 635<=mouse[1]<=700:
                    pygame.quit() 
                if 183<=mouse[0]<=483 and 200<=mouse[1]<=290:
                    display_generator(
                        "easy",
                        screen,
                        position,
                        add_line,
                        color_light,
                        color_dark,
                        color_yellow,
                        color_blue,
                        color_green,
                        color_red,
                        color_red_hover,
                        text_home,
                        text_quit,
                        largefont
                        )
                    return
                if 183<=mouse[0]<=483 and 320<=mouse[1]<=410:
                    display_generator(
                        "medium",
                        screen,
                        position,
                        add_line,
                        color_light,
                        color_dark,
                        color_yellow,
                        color_blue,
                        color_green,
                        color_red,
                        color_red_hover,
                        text_home,
                        text_quit,
                        largefont
                        )
                    return
                if 183<=mouse[0]<=483 and 440<=mouse[1]<=530:
                    display_generator(
                        "hard",
                        screen,
                        position,
                        add_line,
                        color_light,
                        color_dark,
                        color_yellow,
                        color_blue,
                        color_green,
                        color_red,
                        color_red_hover,
                        text_home,
                        text_quit,
                        largefont
                        )
                    return
        pygame.display.update() 