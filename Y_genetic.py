import operator
import numpy as np
import random
import time
random.seed()


class Candidate(object):

    def __init__(self):
        self.values = np.zeros((9, 9), dtype=int)
        self.fitness = None

    def rowFitness(self):
        rowSum = 0
        for i in range(0, 9):
            rowCount = np.zeros(9, dtype=int)
            for j in range(0, 9):
                rowCount[self.values[i][j]-1] += 1

            nonzero = sum(i > 0 for i in rowCount)/9
            rowSum += nonzero
        return rowSum/9

    def columnFitness(self):
        columnSum = 0
        for i in range(0, 9):
            columnCount = np.zeros(9, dtype=int)
            for j in range(0, 9):
                columnCount[self.values[j][i]-1] += 1

            nonzero = sum(i > 0 for i in columnCount)/9
            columnSum += nonzero
        return columnSum/9

    def blockFitness(self):
        blockSum = 0
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                blockCount = np.zeros(9, dtype=int)
                for i_0 in range(i, i+3):
                    for j_0 in range(j, j+3):
                        blockCount[self.values[i_0][j_0]-1] += 1

                nonzero = sum(i > 0 for i in blockCount)/9
                blockSum += nonzero
        return blockSum/9

    def updateFitness(self):

        columnSum = self.columnFitness()
        rowSum = self.rowFitness()
        blockSum = self.blockFitness()
        fitness = columnSum * blockSum * rowSum
        self.fitness = fitness

    def mutation(self, mutationRate, values):

        r = random.uniform(0, 1)
        success = False
        if (r < mutationRate):  # Mutate.
            while(not success):
                row = random.randint(0, 8)
                fromColumn, toColumn = 0, 0
                
                while(fromColumn == toColumn):
                    fromColumn = random.randint(0, 8)
                    toColumn = random.randint(0, 8)

                if(values[row][fromColumn] == 0 and values[row][toColumn] == 0):
                    if(not isColumnDuplicate(values, toColumn, self.values[row][fromColumn]) and not isBlockDuplicate(values, row, fromColumn, self.values[row][toColumn])):
                        if (not isColumnDuplicate(values, fromColumn, self.values[row][toColumn]) and not isBlockDuplicate(values, row, toColumn, self.values[row][fromColumn])):
                            self.values[row][toColumn], self.values[row][fromColumn] = self.values[row][fromColumn], self.values[row][toColumn]
                            success = True
        return success
    
def sort_candidates(candidates):
    return sorted(candidates, key=operator.attrgetter('fitness'), reverse=True)


def seed(Nc, values):
    candidates = []
    temp = Candidate()
    temp.values = []
    for i in range(0, 9):
        temp.values += [[]]
        for _ in range(0, 9):
            temp.values[i] += [[]]
                                     
    for i in range(0, 9*9):
        for value in range(1, 10):
            if((values[i//9][i % 9] == 0)
                and not (isColumnDuplicate(values, i % 9, value)
                         or isBlockDuplicate(values, i//9, i % 9, value)
                         or isRowDuplicate(values, i//9, value))):
                temp.values[i//9][i % 9] += [value]
            elif(values[i//9][i % 9] != 0):
                temp.values[i//9][i % 9] += [values[i//9][i % 9]]
                break

    res = [[[i_0, i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8]
            for i_0 in temp.values[j][0]
            for i_1 in temp.values[j][1]
            for i_2 in temp.values[j][2]
            for i_3 in temp.values[j][3]
            for i_4 in temp.values[j][4]
            for i_5 in temp.values[j][5]
            for i_6 in temp.values[j][6]
            for i_7 in temp.values[j][7]
            for i_8 in temp.values[j][8] if (len(list(set([i_0, i_1, i_2, i_3, i_4, i_5, i_6, i_7, i_8]))) == 9)] for j in range(9)]

    for _ in range(0, Nc):
        g = Candidate()
        g.values = np.array(
            [res[i][random.randint(0, len(res[i])-1)] for i in range(0, 9)])
        candidates += [g]

    for candidate in candidates:
        candidate.updateFitness()
    return candidates


def isRowDuplicate(values, row, value):
    if value in [values[row][column] for column in range(0, 9)]:
        return True
    return False


def isColumnDuplicate(values, column, value):
    if value in [values[row][column] for row in range(0, 9)]:
        return True
    return False


def isBlockDuplicate(values, row, column, value):
    i, j = 3*(row//3), 3*(column//3)
    for i_0 in range(i, i+3):
        for j_0 in range(j, j+3):
            if(values[i_0][j_0] == value):
                return True
    return False


def compete(candidates):
    n = len(candidates)-1
    c1 = candidates[random.randint(0, n)]
    c2 = candidates[random.randint(0, n)]
    f1, f2 = c1.fitness, c2.fitness

    if(f1 > f2):
        fittest, weakest = c1, c2
    else:
        fittest, weakest = c2, c1

    selection_rate = 0.85
    r = random.uniform(0, 1)

    if(r > selection_rate):
        return weakest
    return fittest


def crossover(parent1, parent2, crossoverRate):
    crossoverPoint1 = random.randint(0, 9)
    crossoverPoint2 = random.randint(0, 9)

    maxi = max(crossoverPoint1, crossoverPoint2)
    mini = min(crossoverPoint2, crossoverPoint1)
    if mini == maxi:
        return crossover(parent1, parent2, crossoverRate)

    child1, child2 = Candidate(), Candidate()
    r = random.uniform(0, 1)
    if (r < crossoverRate):
        child1.values = np.copy(parent1.values)
        child2.values = np.copy(parent2.values)
        for i in range(mini, maxi):
            child1.values[i], child2.values[i] = crossoverRows(
                child1.values[i], child2.values[i])
    return child1, child2


def crossoverRows(row1, row2):
    childRow1, childRow2 = np.zeros(9), np.zeros(9)

    while((0 in childRow1) and (0 in childRow2)):
        randx = random.randint(1, 8)
        usedindex = []
        for i in range(0, randx):
            x = random.randint(0, 8)
            if (x not in usedindex):
                childRow1[x] = row2[x]
                childRow2[x] = row1[x]
                usedindex.append(x)

        for i in range(0, 9):
            if (i not in usedindex):
                childRow1[x] = row1[x]
                childRow2[x] = row2[x]

    return childRow1, childRow2


def initialize_params(Nc, given):
    print("seeding Population...")
    phi = 0
    sigma = 1
    mutationRate = 0.5
    candidates = seed(Nc, given)
    return phi, sigma, mutationRate, candidates


def update_params(Nm, phi, sigma):
    phi = 0 if(Nm == 0) else phi / Nm
    sigma = sigma*0.998 if(phi > 0.2) else sigma/0.998
    mutationRate = abs(np.random.normal(loc=0.0, scale=sigma))
    while mutationRate > 1:
        mutationRate = abs(np.random.normal(loc=0.0, scale=sigma))

    return phi, sigma, mutationRate


def solve(given, Nc, Ne, Ng, stale=50):

    Nm, staleCount, prevFitness = 0, 0, 0.0
    phi, sigma, mutationRate, candidates = initialize_params(Nc, given)

    for generation in range(0, Ng):
        nextGeneration, elites = [], []

        print("Generation ", generation)

        candidates = sort_candidates(candidates)
        bestSolution = candidates[0]
        print("Best fitness: ", bestSolution.fitness)

        if(int(bestSolution.fitness) == 1):
            print("Solved at generation ", generation)
            return (bestSolution, generation)

        if generation == 0:
            prevFitness = bestSolution.fitness
            staleCount += 1

        elif prevFitness == bestSolution.fitness:
            staleCount += 1

        elif prevFitness != bestSolution.fitness:
            staleCount = 0
            prevFitness = bestSolution.fitness

        for e in range(0, Ne):
            elite = Candidate()
            elite.values = np.copy(candidates[e].values)
            elites += [elite]

        for _ in range(Ne, Nc, 2):
            parent1 = compete(candidates)
            parent2 = compete(candidates)

            child1, child2 = crossover(parent1, parent2, crossoverRate=1.0)

            for child in [child1, child2]:
                child.updateFitness()
                oldFitness = child.fitness
                success = child.mutation(mutationRate, given)
                child.updateFitness()
                if(success):
                    Nm += 1
                    if(child.fitness > oldFitness):
                        phi = phi + 1
                nextGeneration += [child]

        nextGeneration += elites

        candidates = nextGeneration
        for candidate in candidates:
            candidate.updateFitness()

        phi, sigma, mutationRate = update_params(Nm, phi, sigma)

        if(staleCount >= stale):
            phi, sigma, mutationRate, candidates = initialize_params(Nc, given)
            staleCount = 0
    print("No solution found.")
    return (bestSolution, Ng)


def solution_as_list(matrix):
    sol = []
    for i in range(9):
        row = []
        for a, x in enumerate(matrix[i]):
            row.append(x)
        sol.append(row)
    return sol

def GA_results(initial_matrix):
    Nc = 200  # Number of candidates OR chromosomes(i.e. population size).
    Ne = int(0.6*Nc)  # Number of elites = 120
    Ng = 1500  # Number of generations.
    staleCount = 50
    #given = load_sudoku()
    given  = initial_matrix
    start_time = time.time()
    solution, generation = solve(given, Nc, Ne, Ng, staleCount)
    end_time = time.time()
    time_taken = end_time - start_time
    sudoku_solution = solution_as_list(solution.values)
    return (generation, time_taken, sudoku_solution)