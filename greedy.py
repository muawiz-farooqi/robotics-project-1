#from project import *
import math

#sort the tuples by the tile's manhattan value; choose the one with the lowest cost
#if there is a tie, choose by priority order(Up, Down, Right, Left)
def nextStep(potentialMoves):

    #remove any moves that cross borders and "teleport" to the other side
    realMoves = [move for move in potentialMoves if move[2] >= 0 and move[3] >= 0]
    
    numMoves = len(realMoves)
    
    #sort the moves by manhattan value of the tile
    for i in range(0, numMoves - 1):
        for j in range(0, numMoves - i - 1):
            if realMoves[j][1] > realMoves[j + 1][1]:
                temp = realMoves[j]
                realMoves[j] = realMoves[j + 1]
                realMoves[j + 1] = temp
    
    #return the first tuple of the list  
    return realMoves[0]

#iterate through the workspace to find the goal tile
#goal tile should have a manhattan value of 0
def findGoalTile(workspace):
    for row in range(10):
        for column in range(16):
            if workspace[row][column] == 0:
                return int(row), int(column)


#startingColumn = (0 - 15)
#startingRow = (0 - 9)
def findPath(workspace, startingRow, startingColumn):
    
    initialValue = int(workspace[startingRow][startingColumn])
    path = [("Start", initialValue, startingRow, startingColumn)]

    #starting manhattan value
    tempValue = initialValue  
    tempRow = startingRow
    tempColumn = startingColumn

    #run the next step function until the tile value is 0(the goal)
    while tempValue != 0:
        potentialMoves = [("Up",      int(workspace[tempRow + 1][tempColumn]), tempRow + 1, tempColumn),#up,down,right,left
                          ("Down",    int(workspace[tempRow - 1][tempColumn]), tempRow - 1, tempColumn),
                          ("Right",   int(workspace[tempRow][tempColumn + 1]), tempRow, tempColumn + 1),
                          ("Left",    int(workspace[tempRow][tempColumn - 1]), tempRow, tempColumn - 1)]

        tempTuple = nextStep(potentialMoves)

        #add each step to the list of tuples
        path.append(tempTuple)

        #update tile position and manhattan value of the new tile
        tempRow = tempTuple[2]
        tempColumn = tempTuple[3]
        tempValue = workspace[tempRow][tempColumn]

    #return a list of tuples containing information about the path
    return path