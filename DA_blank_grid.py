from BA_curved_icon import *
from DAA_algo_generator import *
from X_backtracking import *
from X_annealing import *
from X_genetic import *
import time

def dummy():
    pass

def display_generator(
        level,
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
    
    color_white = (255,255,255) 
    minifont = pygame.font.SysFont('Corbel',18)
    mediumfont = pygame.font.SysFont('Corbel',20)
    gridfont = pygame.font.SysFont("comicsans", 42) 
    text_genetic = minifont.render('Genetic' , True , color_white)
    text_simulated = minifont.render('Simulated' , True , color_white)
    text_backtracking = minifont.render('Backtracking' , True , color_white)
    text_annealing = minifont.render('annealing' , True , color_white)
    text_algorithm = minifont.render('algorithm' , True , color_white)
    start_time = time.time()
    initial_matrix = SudokuGenerator(level).generate_puzzle()
    end_time = time.time()
    gen_time_taken = round((end_time - start_time), 4)
    
    new_matrix = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 6, 8, 7, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    text_below1 = mediumfont.render('Time taken to generate sudoku: '+str(gen_time_taken) , True , color_dark)
    text_below2 = mediumfont.render('Do you want to solve this generated sudoku? then choose the algorithm' , True , color_dark)
    
    while True: 
        screen.fill((255,255,255))  
        mouse = pygame.mouse.get_pos()
            
        for i in position:
            for j in position:
                AAfilledRoundedRect(screen,(i, j, add_line, add_line),color_light,0.2)
                
        if 15<=mouse[0]<=130 and 715<=mouse[1]<=775:
            AAfilledRoundedRect(screen,(15, 715, 115, 60),color_light,0.8)
            AAfilledRoundedRect(screen,(145, 715, 115, 60),color_blue,0.8)
            AAfilledRoundedRect(screen,(275, 715, 115, 60),color_green,0.8)
            AAfilledRoundedRect(screen,(406, 715, 115, 60),color_blue,0.8)
            AAfilledRoundedRect(screen,(536, 715, 115, 60),color_red,0.8)
        elif 145<=mouse[0]<=260 and 715<=mouse[1]<=775:
            AAfilledRoundedRect(screen,(15, 715, 115, 60),color_yellow,0.8)
            AAfilledRoundedRect(screen,(145, 715, 115, 60),color_light,0.8)
            AAfilledRoundedRect(screen,(275, 715, 115, 60),color_green,0.8)
            AAfilledRoundedRect(screen,(406, 715, 115, 60),color_blue,0.8)
            AAfilledRoundedRect(screen,(536, 715, 115, 60),color_red,0.8)
        elif 275<=mouse[0]<=391 and 715<=mouse[1]<=775:
            AAfilledRoundedRect(screen,(15, 715, 115, 60),color_yellow,0.8)
            AAfilledRoundedRect(screen,(145, 715, 115, 60),color_blue,0.8)
            AAfilledRoundedRect(screen,(275, 715, 115, 60),color_light,0.8)
            AAfilledRoundedRect(screen,(406, 715, 115, 60),color_blue,0.8)
            AAfilledRoundedRect(screen,(536, 715, 115, 60),color_red,0.8)
        elif 406<=mouse[0]<=521 and 715<=mouse[1]<=775:
            AAfilledRoundedRect(screen,(15, 715, 115, 60),color_yellow,0.8)
            AAfilledRoundedRect(screen,(145, 715, 115, 60),color_blue,0.8)
            AAfilledRoundedRect(screen,(275, 715, 115, 60),color_green,0.8)
            AAfilledRoundedRect(screen,(406, 715, 115, 60),color_light,0.8)
            AAfilledRoundedRect(screen,(536, 715, 115, 60),color_red,0.8)
        elif 536<=mouse[0]<=651 and 715<=mouse[1]<=775:
            AAfilledRoundedRect(screen,(15, 715, 115, 60),color_yellow,0.8)
            AAfilledRoundedRect(screen,(145, 715, 115, 60),color_blue,0.8)
            AAfilledRoundedRect(screen,(275, 715, 115, 60),color_green,0.8)
            AAfilledRoundedRect(screen,(406, 715, 115, 60),color_blue,0.8)
            AAfilledRoundedRect(screen,(536, 715, 115, 60),color_red_hover,0.8)
        else:
            AAfilledRoundedRect(screen,(15, 715, 115, 60),color_yellow,0.8)
            AAfilledRoundedRect(screen,(145, 715, 115, 60),color_blue,0.8)
            AAfilledRoundedRect(screen,(275, 715, 115, 60),color_green,0.8)
            AAfilledRoundedRect(screen,(406, 715, 115, 60),color_blue,0.8)
            AAfilledRoundedRect(screen,(536, 715, 115, 60),color_red,0.8)
        
        screen.blit(text_home, (38, 732))
        screen.blit(text_backtracking, (156, 728))
        screen.blit(text_algorithm, (168, 747))
        screen.blit(text_simulated, (295, 728))
        screen.blit(text_annealing, (298, 747)) 
        screen.blit(text_genetic, (434, 728))
        screen.blit(text_algorithm, (429, 747))
        screen.blit(text_quit, (570, 732))
        screen.blit(text_below1, (180, 664))
        screen.blit(text_below2, (50, 687))
        
        for ev in pygame.event.get():    
            if ev.type == pygame.QUIT: 
                pygame.quit() 
                  
            if ev.type == pygame.MOUSEBUTTONDOWN:     
                if 536<=mouse[0]<=651 and 715<=mouse[1]<=775:
                    pygame.quit() 
                if 15<=mouse[0]<=130 and 715<=mouse[1]<=775:
                    return
                if 145<=mouse[0]<=260 and 715<=mouse[1]<=775:
                    backtracking(
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
                        )
                    return
                if 275<=mouse[0]<=391 and 715<=mouse[1]<=775:
                    annealing(
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
                        )
                    return
                if 406<=mouse[0]<=521 and 715<=mouse[1]<=775:
                    genetic(
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
                        )
                    return
                  
        
        for i in range(9):
            for j in range(9):
                if (initial_matrix[i][j])!=0:
                    AAfilledRoundedRect(screen,(position[i], position[j], add_line, add_line),color_green,0.2)
                    text1 = gridfont.render(str(initial_matrix[i][j]), 1, color_white)
                    screen.blit(text1, (position[i]+25, position[j]+21)) 
        
        pygame.display.update()