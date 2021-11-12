import copy
import time
import random
import numpy as np
count = 0
count_b = 0
possibilities = []
possible = np.empty((9,9))

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
    print("No. of random guess ",count)
    print("No. of Backtracks ",count_b)
def writing_sudoku(matrix):
    stri = ""
    for i in range(9):
        if i%3==0:
            stri +="="*25+"\n"
        for a,x in enumerate(matrix[i]):
            if a%3 == 0:
                stri+="| "
            stri+=str(x)+' '
        stri+="| \n"
    stri+="="*25+"\n"    
    return stri

def is_solved(matrix):
    for i in range(9):
        if sum(matrix[i]) != 45:
            return False
        if sum(np.array(matrix)[:,i]) != 45:
            return False
    return True

def hidden_singles(matrix):
    global possible
    global count
    #finding hidden singles
    for rc in range(9):
            possibles_row = [possible[rc][cell] for cell in range(9)]
            for i in range(1,10):
                poss_row = [x for x,pos in enumerate(possibles_row) if i in pos]
                if len(poss_row) == 1:
                    matrix[rc][poss_row[0]] = i
                    count +=1
                    possible[rc][poss_row[0]] = []
                set_possibilities(matrix)
    for rc in range(9):
            possibles_col = [possible[row][rc] for row in range(9)]
            for i in range(1,10):
                poss_col = [x for x,pos in enumerate(possibles_col) if i in pos]
                if len(poss_col) == 1:
                    matrix[poss_col[0]][rc] = i
                    count+=1
                    possible[poss_col[0]][rc] = []
                set_possibilities(matrix)
                          
def set_possibilities(matrix):
    global possible
    col,row = [],[]
    for i in range(9):
        col = []
        for j in range(9):
            s = update_possibilities(matrix,i,j)
            col.append(s)
            #print(s)
        row.append(col)
    possible = row
    
def find_possibilities(matrix,row,col):  
    return possible[row][col]

def update_possibilities(matrix,row,col):
    global possible
    if matrix[row][col] > 0:
        return {}
    all_s = {i for i in range(1,10)}
    r = {x for x in matrix[row]}
    c = {matrix[i][col] for i in range(9)}
    rc = row - row%3
    cc = col - col%3
    b = {matrix[x][y] for y in range(cc,cc+3) for x in range(rc,rc+3)}
    #print(all - r - c - b)
    return set(all_s - r - c - b)
    
def check_less_cost(matrix):
    l,m,n = [],[],[]
    c = []
    flist = []
    count1,count2,count3 = 0,0,0
    #calculating the total no. of entries in row/column/boxes
    for i in range(9):
        count1,count2 = 0, 0
        for j in range(9):
            if matrix[i][j]>0:
                count1+=1
            if matrix[j][i]>0:
                count2+=1
        n.append(count1)
        l.append(count2)
    
    for a in range(9):
        for b in range(9):
            c.append(n[a]+l[b])
    #choose the empty cell with high cost
    x = np.argsort(c)
    for u in reversed(x):
        if(matrix[u//9][u%9] == 0):
            return u//9,u%9
    if is_solved(matrix):
        return (9,9)
    return (10,10)

def check_safe(matrix,row,col,num):
    global count
    #check if num in row
    if num in matrix[row]:
        return False
    #check if num in column
    for x in range(9):
        if num == matrix[x][col]:
            return False
    #check if num in box
    r = row - row%3
    c = col - col%3
    for x in range(r,r+3):
        for y in range(c,c+3):
            if num == matrix[x][y]:
                return False
    count += 1
    return True

def solver(matrix):
    global count,count_b
    r,c = check_less_cost(matrix)
    if r == 9:
        return matrix
    for i in find_possibilities(matrix,r,c):
        matrix[r][c] = i
        set_possibilities(matrix)
        count += 1
        result = solver(matrix)
        if result:
            return True
    matrix[r][c] = 0
    count_b+=1
    set_possibilities(matrix)
    return False

def deep_solver1(matrix):
    global count
    global count_b
    #find next empty location
    r,c = next_loc(matrix)
    if r == 9:
        return matrix
    # Checking neighbor state
    for i in find_possibilities(matrix,r,c):
        ## Forward checking
        c_matrix = copy.deepcopy(matrix)
        c_matrix[r][c] = i
        set_possibilities(c_matrix)
        # Fill Single possible values
        fill_one(c_matrix)
        count += 1
        #print("dddd",count)
        result = deep_solver(c_matrix)
        if result:
            return result
    #backtracking
    set_possibilities(matrix)
    count_b+=1
    return None

def deep_solver(matrix):
    global count,count_b
    #find the empty place with less no. of elements in row/column/box
    r,c = check_less_cost(matrix)
    if r == 9:
        return matrix
    if r == 10:
        print("Some Error Occured")
    # Checking neighbor state
    for i in find_possibilities(matrix,r,c):
        ## Forward checking
        c_matrix = copy.deepcopy(matrix)
        c_matrix[r][c] = i
        count += 1
        set_possibilities(c_matrix)
        # Fill Single possible values
        fill_one(c_matrix)
        #Fill Hidden pair
        hidden_pair(c_matrix)
        #recursive solver using deep copy
        result = deep_solver(c_matrix)
        if result:
            return result
    #backtracking
    set_possibilities(matrix)
    count_b+=1
    return None

def next_loc(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j]==0:
                return (i,j)
    return (9,9)


def fill_one(matrix):
    flag = True
    global count
    sub_matrix = copy.deepcopy(matrix)
    while(flag):
        hidden_singles(matrix)
        flag = False
        for i in range(9):
            for j in range(9):
                if matrix[i][j]==0:
                    #checking if there is only one possibility
                    x = find_possibilities(matrix,i,j)
                    if len(x)== 1:
                        for l in x:
                            count += 1
                            #print(count,"count fill")
                            matrix[i][j] = l
                            set_possibilities(matrix)
        if sub_matrix != matrix:
            sub_matrix = copy.deepcopy(matrix)
            flag  = True
                        
def write_initial_report(data,x):
    first = ["="*3+"Team Valorant"+"="*3+"\n","Team Members "," * Jigar Makwana"," * Sandeep Parihar"," * Snehlata Yadav"," * Sawan"]
    with open("report_copy.txt",'w') as file:
        for line in first:
            file.write(line+"\n")
        file.write(" "*7+"This is the Initial Sudoku Board\n")
        for lines in writing_sudoku(data).split("\n"):
            file.write(" "*10+lines+"\n")
        file.write("=:"*40+"=\n")
        file.write("Empty cells in grid "+str(len([ 0  for i in x  if i == '.'])))
    
        
def write_simple_report(data,time,mode,count):
    
    with open("report_copy.txt","a+") as file:
        file.write("\nSolved Sudoku Board Using "+mode+"\n")
        if data==None:
            file.write("\n\n ***Failed to solve the sudoku*** \n\n")
            pass
        for lines in writing_sudoku(data).split("\n"):
            file.write(" "*10+lines+"\n")
        #file.writelines(writing_sudoku(data))
        file.write("\nNo of random guesses "+str(count)+"\n")
        file.write("\nNo of Backtracks "+str(count_b)+"\n")
        file.write("It took %.4f seconds to solve the problem\n"%time)
        file.write("=+"*40+"=\n")
        
        
        

def hidden_pair(matrix):
    global possible
    for row in range(9):
        done = []
        for i in range(1,10):
            if i in done:
                continue
            pos=[]
            for cell in range(9):
                if i in possible[row][cell]:
                    pos.append(cell)
            if len(pos)!=2:
                continue
            hidden = []
            
            for j in range(1,10):
                hidden = []
                if i==j:
                    continue
                for x in range(9):
                    if j in possible[row][x]:
                        hidden.append(x)
                if len(hidden)==2 and pos==hidden:
                    done.append(j)
                    possible[row][hidden[0]] = {i,j}
                    possible[row][hidden[1]] = {i,j}
          
    for col in range(9):
        done = []
        for i in range(1,10):
            pos=[]
            if i in done:
                continue
            for cell in range(9):
                if i in possible[cell][col]:
                    pos.append(cell)
            if len(pos)!=2:
                continue
            
            for j in range(1,10):
                hidden = []
                if i==j:
                    continue
                for x in range(9):
                    if j in possible[x][col]:
                        hidden.append(x)
                if len(hidden)==2 and pos==hidden:
                    done.append(j)
                    possible[hidden[0]][col] = {i,j}
                    possible[hidden[1]][col] = {i,j}

def Stage(grid):
    set_possibilities(grid)
    
    result = deep_solver(grid)
    return (result, count)

def time_take(grid):
    start_time = time.time()
    solve_grid = Stage(grid)
    end_time = time.time()
    time_taken = end_time-start_time
    return time_taken

#grid = [[0, 0, 0, 4, 0, 0, 5, 6, 0], [0, 1, 0, 5, 0, 6, 0, 9, 0], [0, 0, 0, 0, 9, 7, 3, 0, 0], [0, 0, 9, 0, 2, 0, 0, 4, 0], [6, 0, 0, 0, 0, 5, 0, 0, 0], [0, 0, 0, 3, 7, 0, 0, 0, 0], [5, 0, 2, 0, 0, 0, 0, 0, 0], [0, 6, 3, 0, 0, 0, 0, 0, 0], [0, 0, 0, 9, 6, 0, 8, 0, 0]]

#start_time = time.time()
#solve_grid = Stage(grid)
#end_time = time.time()

# you have all three values here required you can use it.
#print(grid)
#print(solve_grid)
#print(end_time-start_time,"time taken")
#print(count)



