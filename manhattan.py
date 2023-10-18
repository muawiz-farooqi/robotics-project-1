# Breadth-first Manhattan distance workspace generator
import math


def index_2d(arr, value, indexes):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == value:
                if (i,j) not in indexes:
                    return(i,j)
                

def bfs_manhattan(workspace):
    # start at goal
    curr_dist = 0
    populated = False

    while populated == False:
        # find curr position
        indexes  = []
        curr_pos = index_2d(workspace, curr_dist, indexes)
        if curr_pos != None:
            indexes.append(curr_pos)
        # print(curr_dist)
        # loop through all positions with dist = curr_dist
        while curr_pos != None:
            # print('looping...')
            if curr_pos[0] > 0:
                if workspace[curr_pos[0]-1][curr_pos[1]] == -1:
                    workspace[curr_pos[0]-1][curr_pos[1]] = curr_dist+1
            if curr_pos[0] < 9:
                if workspace[curr_pos[0]+1][curr_pos[1]] == -1:
                    # print('replacing...')
                    workspace[curr_pos[0]+1][curr_pos[1]] = curr_dist+1
                    # print('replaced!')
            if curr_pos[1] > 0:
                if workspace[curr_pos[0]][curr_pos[1]-1] == -1:
                    workspace[curr_pos[0]][curr_pos[1]-1] = curr_dist+1
            if curr_pos[1] < 15:
                if workspace[curr_pos[0]][curr_pos[1]+1] == -1:
                    workspace[curr_pos[0]][curr_pos[1]+1] = curr_dist+1

            curr_pos = index_2d(workspace, curr_dist, indexes)
            # print(curr_pos)
            if curr_pos != None:
                indexes.append(curr_pos)

        if index_2d(workspace, -1, []) == None:
            populated = True
            break
        else:
            # print_space(workspace)
            populated = False

        # increment distance
        curr_dist += 1



