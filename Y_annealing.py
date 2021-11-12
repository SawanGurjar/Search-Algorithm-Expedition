import copy
import random
import time
import numpy as np
from matplotlib import pyplot as plt
from simanneal import Annealer
def printing_sudoku(matrix):
    for i in range(9):
        if i%3==0:
            print("="*25)
        for a,x in enumerate(matrix[i]):
            if a%3 == 0:
                print(end="| ")
            print(x,end=' ')
        print("| ")
    print("="*25)    

def testcase():
    #################provide your input hereeee##########################
    x = '...4..56..1.5.6.9.....973....9.2..4.6....5......37....5.2.......63.........96.8..'
    global count
    count = 0
    data = [ 0 if i == '.' else i for i in x ]
    #print(data)
    matrix = []
    row = []
    for i,x in enumerate(data):
        row.append(int(x))
        if(i%9 == 8):
            matrix.append(row)
            row = []
    #print(np.array(matrix))
    return np.array(matrix)

def init_matrix(matrix):
    unIndex = []
    for block in range(9):
        index,value = empty_cell_value(block,matrix)
        unIndex.append(index)
        unfilled_value = [n for n in range(1,10) if n not in value]
        random.shuffle(unfilled_value)
        for (a,b),x in zip(index,unfilled_value):
            matrix[a][b] = x
    return matrix,unIndex
            
def empty_cell_value(N,matrix):
    start_row = (N//3)*3
    start_col = (N%3)*3
    #print(start_row,start_col,matrix[start_row][start_col])
    filled = []
    index = []
    for i in range(start_row,start_row+3):
        for j in range(start_col,start_col+3):
            if matrix[i][j] == 0:
                index.append((i,j))
            else:
                filled.append(matrix[i][j])
    #print("indexin",index)
    return index,filled
    
def choose_two(index):
    #randomly pick a block
    block = random.randint(0,8)
    #print(block)
    #print("block",index[block])
    n1,n2 = random.sample(index[block],2)
    
    return n1,n2

class Sudoku_Row(Annealer):
    def __init__(self,matrix):
        state,self.unindex = init_matrix(matrix)
        super().__init__(state)
    def move(self):
        i1,i2 = choose_two(self.unindex)
        x,y = i1
        a,b = i2
        self.state[x,y], self.state[a,b] = self.state[a,b], self.state[x,y]
    def energy(self):
        column_score = lambda n: -len(set(self.state[i, n] for i in range(9)))
        row_score = lambda n: -len(set(self.state[n,i] for i in range(9)))
        score = sum(column_score(n)+row_score(n) for n in range(9))
        arr.append(score)
        if score == -162:
            self.user_exit = True
        return score
        
def Stage(matrix):
    global arr
    arr = []
    start_time = time.time()
    
    sudoku = Sudoku_Row(matrix)
    sudoku.copy_strategy = "method"
    sudoku.Tmax = 0.5
    sudoku.Tmin = 0.05
    sudoku.steps = 10000
    #sudoku.updates = 100
    state, e = sudoku.anneal()
    end_time = time.time()
    time_taken = end_time-start_time

    return state,e, time_taken