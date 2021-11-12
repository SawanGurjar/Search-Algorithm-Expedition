from BA_curved_icon import *
from Y_backtracking import *
#import A_main

def dummy():
    pass

def backtracking(
        initial_matrix,
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
        ):
    
    new_matrix, count = Stage(initial_matrix)    
    time_taken = time_take(initial_matrix)
    time_taken = round(time_taken,4)
    
    color_white = (255,255,255) 
    mediumfont = pygame.font.SysFont('Corbel',20)
    gridfont = pygame.font.SysFont("comicsans", 42) 
    algo_name = largefont.render('Backtracking algorithm' , True , color_white)
    
    #count = 0
    #new_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 6, 8, 7, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    text_below1 = mediumfont.render('Number of random guesses: '+str(count) , True , color_dark)
    text_below2 = mediumfont.render('Time taken: '+str(time_taken) , True , color_dark)
    
    while True: 
        screen.fill((255,255,255))  
        mouse = pygame.mouse.get_pos()
            
        for i in position:
            for j in position:
                AAfilledRoundedRect(screen,(i, j, add_line, add_line),color_light,0.2)
                
        if 21<=mouse[0]<=161 and 715<=mouse[1]<=775:
            AAfilledRoundedRect(screen,(21, 715, 140, 60),color_light,0.8)
            AAfilledRoundedRect(screen,(182, 715, 302, 60),color_light,0.8)
            AAfilledRoundedRect(screen,(505, 715, 140, 60),color_red,0.8)
        elif 505<=mouse[0]<=645 and 715<=mouse[1]<=775:
            AAfilledRoundedRect(screen,(21, 715, 140, 60),color_yellow,0.8)
            AAfilledRoundedRect(screen,(182, 715, 302, 60),color_light,0.8)
            AAfilledRoundedRect(screen,(505, 715, 140, 60),color_red_hover,0.8)
        else:
            AAfilledRoundedRect(screen,(21, 715, 140, 60),color_yellow,0.8)
            AAfilledRoundedRect(screen,(182, 715, 302, 60),color_light,0.8)
            AAfilledRoundedRect(screen,(505, 715, 140, 60),color_red,0.8)
        
        screen.blit(text_home, (63, 732))
        screen.blit(algo_name, (205, 732))
        screen.blit(text_quit, (548, 732))
        screen.blit(text_below1, (209, 664))
        screen.blit(text_below2, (260, 687))
        
        for ev in pygame.event.get():    
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                  
            if ev.type == pygame.MOUSEBUTTONDOWN:     
                if 505<=mouse[0]<=645 and 715<=mouse[1]<=775:
                    pygame.quit() 
                if 21<=mouse[0]<=161 and 715<=mouse[1]<=775:
                    return
                
        for i in range(9):
            for j in range(9):
                if (initial_matrix[i][j])!=0:
                    AAfilledRoundedRect(screen,(position[i], position[j], add_line, add_line),color_green,0.2)
                    text1 = gridfont.render(str(initial_matrix[i][j]), 1, color_white)
                else:
                    AAfilledRoundedRect(screen,(position[i], position[j], add_line, add_line),color_blue,0.2)
                    text1 = gridfont.render(str(new_matrix[i][j]), 1, color_white)
                screen.blit(text1, (position[i]+25, position[j]+21)) 
        
        pygame.display.update()
