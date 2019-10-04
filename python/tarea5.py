import random

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def generateMatrix(m,n,randomInit,randomEnd):
    resultsMatrix = [[random.randint(randomInit,randomEnd) for i in range(n) ] for j in range(m)]
    return resultsMatrix

def getMatrixMult(randomInit,randomEnd,m,n,p):
    matrix1= generateMatrix(m,n,randomInit,randomEnd)
    matrix2 = generateMatrix(n,p,randomInit,randomEnd)
    print("Print Matrix 1")
    printMatrix(matrix1)
    print("\nPrint Matrix 2")
    printMatrix(matrix2)
    resultsMatrix = [[0 for i in range(p) ] for j in range(m)]
    for i in range(m):
        for j in range(p):
            temRes = 0
            for w in range(n):
                temRes = temRes+(matrix1[i][w]*matrix2[w][j])
                resultsMatrix[i][j]= temRes
    print("\nPrint Matrix Res")
    printMatrix(resultsMatrix)
def getMatrixMultUser():
    randomInit = input("Inserte el valor aleatorio minimo: ")
    randomEnd = input("Inserte el valor aleatorio maximo: ")
    m = input("Inserte la cantidad de filas matriz 1: ")
    n = input("Inserte la cantidad de columnas matriz 1: ")
    p = input("Inserte la cantidad de filas matriz 2: ")
    getMatrixMult(randomInit,randomEnd,m,n,p)
    
getMatrixMultUser()