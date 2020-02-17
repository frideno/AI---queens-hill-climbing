import random
import numpy as np


'''
function to count threats - number of column and diagonial threats.
queens is array length n, which queens[row i] = column to put queen.
'''

def count_threats(queens):
    counter = 0
    for i in range(len(queens)):
        for j in range(i+1, len(queens)):
            qi, qj = queens[i], queens[j]
            if qi == qj: counter += 1
            if abs(j-i) == abs(qi-qj): counter += 1
    return counter


'''
hill climbing algorithm. each step takes random queen and give it the column of which gives the lowest threates number after. 
the algorithm stops iterating when there is no improvment in number of threats.
'''
def hill_climb(init):
    n = len(init)
    current_min = count_threats(init)
    queens = init[:]
    while True:
        scores = []
        i = random.randint(0, n-1)
        for qi in range(n):
            queens[i] = qi
            scores.append(count_threats(queens))
        best_qi = scores.index(min(scores))
        queens[i] = best_qi
        if min(scores) == current_min:
            break
        current_min = min(scores)
    return queens

'''
the solve function. given n, init random n sized board, and hill climb on that. 
do it n^3 times, and take the solution with minimum threats, to make sure that it finds a solution with 0 threats.
'''
def solve_queens(n):
    queens_starts = []
    for i in range(n**3):
        queens_starts.append([random.randint(0, n-1) for j in range(n)])
    minerr = float('inf')
    for queens in queens_starts:
        solution = hill_climb(queens)
        err = count_threats(solution)
        if err < minerr:
            bestsol = solution
            minerr = err
    return matrixit(bestsol), minerr

'''
function to visualize the array, in the shape of board.
'''
def matrixit(arr):
    n = len(arr)
    m = np.zeros((n, n))
    for i,v in enumerate(arr):
        m[i][v] = 1
    return m

# main:
solve_queens(8)
    
