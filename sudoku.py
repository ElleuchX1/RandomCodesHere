import numpy as np
import random
def possible(x,y,n,Sudo):
    # Vérification des cols + rows
    for i in range(0,9):
        if Sudo[x][i]== n:
            return False

    for i in range(0,9):
        if Sudo[i][y]==n:
            return False
    
    # Vérification des blocs contenant (x,y)
    new_x=(x//3)*3
    new_y=(y//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if Sudo[new_x+i][new_y+j]==n:
                return False
    return True

def Generate_Random_Sudoku():
    
    Sud=np.zeros((9,9))
    init_Cord=[]
    i=1
    while i<18:
        a=(random.randrange(1, 9), random.randrange(1, 9))
        if a not in init_Cord:
            init_Cord.append(a)
            i+=1  
    print(init_Cord)
    init_num=1
    C1=random.randrange(1, 9)
    
    for C in init_Cord:
        print(C1)
        while not ( possible(C[0],C[1],C1,Sud)):
            C1=random.randrange(1, 9)
        
        Sud[C[0]][C[1]]=C1
             
    return Sud

def Solve_Sud(A):
    for i in range(9):
        for j in range(9):
            if A[i][j] == 0:
                for  n in range(1,10):
                    if possible(i,j,n,A):
                        A[i][j]=n
                        Solve_Sud(A)
                        A[i][j]=0
                return A


A=Generate_Random_Sudoku()
print(A)
print(Solve_Sud(A))





