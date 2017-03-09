#!/usr/bin/env python3

import Line

# Prints a matrix somewhat nicely
def printMatrix(matrix):
    printString = ''
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range (0, rows):
        for j in range (0, columns):
            printString = printString + str(matrix[i][j]) + ' '
        printString = printString + '\n'
    print(printString)

# Performs scalar multiplication on a matrix
def scalarMultiplication(scalar, matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    for row in range(0, rows):
        for column in range(0, columns):
            matrix[row][column] = matrix[row][column] * scalar

## Test if this works with matrices of other dimensions
# This function is specific to 4xN edge matrix multiplied BY a 4x4 matrix
# Multiplier, Multiplicand

# really buggy, can't get it to change the variable outside of function
def matrixMultiplication(matrix, edgeMatrix):
    if len(matrix[0]) != len(edgeMatrix):
        print('matrices cannot be multiplied.')
        return false
    retMatrix = []
    tempList = []
    for row in range(0, len(matrix)):
        retMatrix.append([])
        for column in range(0, len(edgeMatrix[row])):
            for i in range(0, len(edgeMatrix)):
                tempList.append(edgeMatrix[i][column])
            retMatrix[row].append(dotProduct(matrix[row], tempList))
            tempList = []
    # Force edge matrix to take the value of retMatrix
    return retMatrix[:]
            

# Helper function for matrix multiplication         
def dotProduct(list1, list2):
    dotProduct = 0
    if len(list1) != len(list2):
        print('lists of unequal lengths')
        return false
    for i in range(0, len(list1)):
        dotProduct = dotProduct + (list1[i] * list2[i])
    return dotProduct

# Returns identity matrix of a given matrix
def getIdentityMatrix(matrix):
    length = max(len(matrix), len(matrix[0]))
    retMatrix = []
    for r in range(0, length):
        retMatrix.append([])
        for c in range(0, length):
            if(r == c):
                retMatrix[r].append(1)
            else:
                retMatrix[r].append(0)
    return retMatrix

# Adds a point to edgeMatrix
def addPoint(matrix, a):
    matrix[0].append(a[0])
    matrix[1].append(a[1])
    matrix[2].append(a[2])
    matrix[3].append(1)

# Adds an edge to edgeMatrix using addPoint
def addEdge(matrix, a, b):
    addPoint(matrix, a)
    addPoint(matrix, b)

# Draws all the edges of edgeMatrix to screen with color
# Typecasts all floats to rounded ints for drawLine function
# They remain floats in the edgeMatrix
def drawEdges(screen, edgeMatrix, color):
    for i in range(0, len(edgeMatrix[0]) - 1, 2):
        Line.drawLine(screen, [int(round(edgeMatrix[0][i])), int(round(edgeMatrix[1][i]))], [int(round(edgeMatrix[0][i+1])), int(round(edgeMatrix[1][i+1]))], color)
