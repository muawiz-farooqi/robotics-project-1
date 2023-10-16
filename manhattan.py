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


# def print_space(workspace):
#     for i in range(10):
#         print(workspace[i])
    
# MAX_OBSTACLES = 25
# obstacles = [[0 for x in range(2)] for y in range(MAX_OBSTACLES)]
# obstacles[0] = [0.61, 2.743]
# obstacles[1] = [0.915, 2.743]
# obstacles[2] = [1.219, 2.743]
# obstacles[3] = [1.829, 1.219]
# obstacles[4] = [1.829, 1.524]
# obstacles[5] = [1.829, 1.829]
# obstacles[6] = [1.829, 2.134]
# obstacles[7] = [2.743, 0.305]
# obstacles[8] = [2.743, 0.61]
# obstacles[9] = [2.743, 0.915]
# obstacles[10] = [2.743, 2.743]
# obstacles[11] = [3.048, 2.743]
# obstacles[12] = [3.353, 2.743]
# obstacles[13] = [-1, -1]
# obstacles[14] = [-1, -1]
# obstacles[15] = [-1, -1]
# obstacles[16] = [-1, -1]
# obstacles[17] = [-1, -1]
# obstacles[18] = [-1, -1]
# obstacles[19] = [-1, -1]
# obstacles[20] = [-1, -1]
# obstacles[21] = [-1, -1]
# obstacles[22] = [-1, -1]
# obstacles[23] = [-1, -1]
# obstacles[24] = [-1, -1]
# goal = [3.658, 1.829]
# workspace = [[-1 for x in range(16)] for y in range(10)]
# workspace[math.ceil(goal[1]/0.305)][math.ceil(goal[0]/0.305)] = 0
# for obstacle in obstacles:
#   if obstacle[0] == -1:
#     continue
#   x = math.ceil(obstacle[0]/0.305)
#   y = math.ceil(obstacle[1]/0.305)
#   workspace[y][x] = 1000
# for i in range(10):
#     print(workspace[i])
# print()
# print()
# bfs_manhattan(workspace)
# print_space(workspace)

