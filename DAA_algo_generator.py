from random import shuffle, randint
import copy

class SudokuGenerator:
    def __init__(self, level):
        self.counter = 0
        self.path = []
        self.grid = [[0 for i in range(9)] for j in range(9)]
        self.level = level
        self.filled_cell = 0
        self.generate_puzzle()    

    def generate_puzzle(self):
        """generates a new puzzle and solves it"""
        if self.level == "easy":
            self.filled_cell = randint(36, 50)
        elif self.level == "medium":
            self.filled_cell = randint(27, 35)
        elif self.level == "hard":
            self.filled_cell = randint(19, 26)
        self.generate_solution(self.grid)
        self.remove_numbers_from_grid()
        return self.grid

    def generate_solution(self, grid):
        """generates a full solution with backtracking"""
        number_list = [1,2,3,4,5,6,7,8,9]
        for i in range(0,81):
            row=i//9
            col=i%9
            #find next empty cell
            if grid[row][col]==0:
                shuffle(number_list)      
                for number in number_list:
                    if self.valid_location(grid,row,col,number):
                        self.path.append((number,row,col))
                        grid[row][col]=number
                        if not self.find_empty_square(grid):
                            return True
                        else:
                            if self.generate_solution(grid):
                                #if the grid is full
                                return True
                break
        grid[row][col]=0  
        return False

    def remove_numbers_from_grid(self):
        """remove numbers from the grid to create the puzzle"""
        #get all non-empty squares from the grid
        non_empty_squares = self.get_non_empty_squares(self.grid)
        non_empty_squares_count = len(non_empty_squares)
        rounds = 3
        while rounds > 0 and non_empty_squares_count >= self.filled_cell:
            #there should be at least 17 clues
            row,col = non_empty_squares.pop()
            non_empty_squares_count -= 1
            #might need to put the square value back if there is more than one solution
            removed_square = self.grid[row][col]
            self.grid[row][col] = 0
            #make a copy of the grid to solve
            grid_copy = copy.deepcopy(self.grid)
            #initialize solutions counter to zero
            self.counter=0      
            self.solve_puzzle(grid_copy)   
            #if there is more than one solution, put the last removed cell back into the grid
            if self.counter!=1:
                self.grid[row][col]=removed_square
                non_empty_squares_count += 1
                rounds -=1
        return

    def find_empty_square(self,grid):
        """return the next empty square coordinates in the grid"""
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i,j)
        return

    def solve_puzzle(self, grid):
        """solve the sudoku puzzle with backtracking"""
        for i in range(0,81):
            row=i//9
            col=i%9
            #find next empty cell
            if grid[row][col]==0:
                for number in range(1,10):
                    #check that the number hasn't been used in the row/col/subgrid
                    if self.valid_location(grid,row,col,number):
                        grid[row][col]=number
                        if not self.find_empty_square(grid):
                            self.counter+=1
                            break
                        else:
                            if self.solve_puzzle(grid):
                                return True
                break
        grid[row][col]=0  
        return False

    def get_non_empty_squares(self,grid):
        """returns a shuffled list of non-empty squares in the puzzle"""
        non_empty_squares = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] != 0:
                    non_empty_squares.append((i,j))
        shuffle(non_empty_squares)
        return non_empty_squares


    def num_used_in_row(self,grid,row,number):
        if number in grid[row]:
            return True
        return False

    def num_used_in_column(self,grid,col,number):
        for i in range(9):
            if grid[i][col] == number:
                return True
        return False

    def num_used_in_subgrid(self,grid,row,col,number):
        sub_row = (row // 3) * 3
        sub_col = (col // 3)  * 3
        for i in range(sub_row, (sub_row + 3)): 
            for j in range(sub_col, (sub_col + 3)): 
                if grid[i][j] == number: 
                    return True
        return False

    def valid_location(self,grid,row,col,number):
        if self.num_used_in_row(grid, row,number):
            return False
        elif self.num_used_in_column(grid,col,number):
            return False
        elif self.num_used_in_subgrid(grid,row,col,number):
            return False
        return True
