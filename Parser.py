#!~usr/bin/env python3

import Screen
import Line
import Matrix
import Transform
import random

def parseFile(fileName, screen, color, edgeMatrix, transformMatrix):
    # with as closes file automatically, reopen after number of lines is got
    # with open('{}'.format(fileName), 'r') as scriptFile:
    #     num_lines = sum(1 for line in scriptFile)
    scriptFile = open('{}'.format(fileName), 'r')
    for line in scriptFile:
        line = line.split()
        transformMatrix = completeCommand(scriptFile, screen, color, line, edgeMatrix, transformMatrix)
        print(line[0])
        Matrix.printMatrix(transformMatrix)
        Matrix.printMatrix(edgeMatrix)

def completeCommand(scriptFile, screen, color, commandLine, edgeMatrix, transformMatrix):
    if(commandLine[0] == 'line'):
        argumentLine = scriptFile.readline().split()
        return doLine(argumentLine, edgeMatrix, transformMatrix)
        
    elif(commandLine[0] == 'ident'):
        return doIdent(transformMatrix)
        
    elif(commandLine[0] == 'move'):
        argumentLine = scriptFile.readline().split()
        return doMove(argumentLine, transformMatrix)
        
    elif(commandLine[0] == 'scale'):
        argumentLine = scriptFile.readline().split()
        return doScale(argumentLine, transformMatrix)
        
    elif(commandLine[0] == 'rotate'):
        argumentLine = scriptFile.readline().split()
        return doRotate(argumentLine, transformMatrix)
        
    elif(commandLine[0] == 'apply'):
        return doApply(screen, color, edgeMatrix, transformMatrix)
        
    elif(commandLine[0] == 'display'):
        return doDisplay(screen, color, edgeMatrix, transformMatrix)
        
    elif(commandLine[0] == 'save'):
        argumentLine = scriptFile.readline().split()
        return doSave(screen, color, argumentLine, edgeMatrix, transformMatrix)
        
    else:
        print('invalid command: {}'.format(commandLine[0]))

def doLine(argumentLine, edgeMatrix, transformMatrix):
    a = [ int(argumentLine[0]), int(argumentLine[1]), int(argumentLine[2]) ]
    b = [ int(argumentLine[3]), int(argumentLine[4]), int(argumentLine[5]) ]
    Matrix.addEdge(edgeMatrix, a, b)
    return transformMatrix
    
def doIdent(transformMatrix):
    return Matrix.getIdentityMatrix(transformMatrix)
   
def doMove(argumentLine, transformMatrix):
    moveMatrix = Transform.createTranslateMatrix( int(argumentLine[0]), int(argumentLine[1]), int(argumentLine[2]))
    return Matrix.matrixMultiplication(moveMatrix, transformMatrix)

def doScale(argumentLine, transformMatrix):
    scaleMatrix = Transform.createScaleMatrix( int(argumentLine[0]), int(argumentLine[1]), int(argumentLine[2]) )
    return Matrix.matrixMultiplication(scaleMatrix, transformMatrix)
    
def doRotate(argumentLine, transformMatrix):
    rotateMatrix = Transform.createRotateMatrix(argumentLine[0], int(argumentLine[1]))
    return Matrix.matrixMultiplication(rotateMatrix, transformMatrix)

def doApply(screen, color, edgeMatrix, transformMatrix):
    # edgeMatrix should remain unchanged.
    newMatrix = Matrix.matrixMultiplication(transformMatrix, edgeMatrix)[:]
    Matrix.drawEdges(screen, newMatrix, color)
    return transformMatrix

def doDisplay(screen, color, edgeMatrix, transformMatrix):
    filename = random.random()
    Screen.writePpmFile(screen, '{}'.format(filename), filename)
    print('WIP')
    print('open {}'.format(filename))
    return transformMatrix

def doSave(screen, color, argumentLine, edgeMatrix, transformMatrix):
    Screen.writePpmFile(screen, '{}'.format(argumentLine[0]), 'z')
    return transformMatrix


