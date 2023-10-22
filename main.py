#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from turn_robot import *
from forward_robot import forward_robot

from manhattan import *
from greedy import *

import math
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
right_motor = Motor(Port.A)
left_motor = Motor(Port.D)
gyro = GyroSensor(Port.S3)


MAX_OBSTACLES = 25
obstacles = [[0 for x in range(2)] for y in range(MAX_OBSTACLES)]
obstacles[0] = [0.61, 2.743]
obstacles[1] = [0.915, 2.743]
obstacles[2] = [1.219, 2.743]
obstacles[3] = [1.829, 1.219]
obstacles[4] = [1.829, 1.524]
obstacles[5] = [1.829, 1.829]
obstacles[6] = [1.829, 2.134]
obstacles[7] = [2.743, 0.305]
obstacles[8] = [2.743, 0.61]
obstacles[9] = [2.743, 0.915]
obstacles[10] = [2.743, 2.743]
obstacles[11] = [3.048, 2.743]
obstacles[12] = [3.353, 2.743]
obstacles[13] = [-1, -1]
obstacles[14] = [-1, -1]
obstacles[15] = [-1, -1]
obstacles[16] = [-1, -1]
obstacles[17] = [-1, -1]
obstacles[18] = [-1, -1]
obstacles[19] = [-1, -1]
obstacles[20] = [-1, -1]
obstacles[21] = [-1, -1]
obstacles[22] = [-1, -1]
obstacles[23] = [-1, -1]
obstacles[24] = [-1, -1]

# Goal and start positions
goal = (3.658, 1.829)
start = [0.305, 1.219]
workspace = [[-1 for x in range(16)] for y in range(10)]

#Inserting Goal
workspace[math.ceil(goal[1]/0.305)][math.ceil(goal[0]/0.305)] = 0 

for obstacle in obstacles:
  if obstacle[0] == -1:
    continue
  x = math.ceil(obstacle[0]/0.305)
  y = math.ceil(obstacle[1]/0.305)
  workspace[y][x] = 1000
#print(obstacles)

for line in reversed(workspace):
  print(line)
bfs_manhattan(workspace)
print()
for line in workspace:
  print(line)

path = findPath(workspace, math.ceil(start[1]/0.305), math.ceil(start[0]/0.305) )
print(path)

# Write your program here.
#ev3.speaker.beep()
gyro.reset_angle(0)
left_motor.reset_angle(0)
right_motor.reset_angle(0)

test_path = [('Left',1),('Right',1)]
test_path2 = [('Start'), 
('Up'), 
('Right'), 
('Right'), 
('Right'), 
('Right'), 
('Right'), 
('Right'), 
('Down'), 
('Down'), 
('Down'), 
('Right'), 
('Right'), 
('Right'), 
('Right'), 
('Right')]

for direction in path:
  # skips the 'Start' direction
  if direction[0] == 'Start':
    continue
  print(direction[0])
  print("Starting of instruction: " + str(gyro.angle()))
  if direction[0] == 'Up':
    while(gyro.angle() != -90):
      print(">>" + str(gyro.angle()))
      if gyro.angle() >-90:
        turn_robot('left', gyro, left_motor, right_motor, -90)
      elif gyro.angle() <-90:
        turn_robot('right', gyro, left_motor, right_motor, -90)
    target_angle = -90  
  elif direction[0] == 'Down':
    while(gyro.angle() != 90):
      print(">>" + str(gyro.angle()))
      if gyro.angle() > 90:
        turn_robot('left', gyro, left_motor, right_motor, 90) 
      elif gyro.angle() < 90:
        turn_robot('right', gyro, left_motor, right_motor, 90)
    target_angle = 90
  elif direction[0] == 'Right':
    while(gyro.angle() != 0):
      print(">>" + str(gyro.angle()))
      if gyro.angle() < 0:
        turn_robot('right', gyro, left_motor, right_motor, 0)
      elif gyro.angle() > 0:
        turn_robot('left', gyro, left_motor, right_motor , 0)
    target_angle = 0
  elif direction[0] == 'Left':
    while(gyro.angle() != 180):
      print(">>" + str(gyro.angle()))
      if gyro.angle() > 180:
        turn_robot('left', gyro, left_motor, right_motor, 180) 
      elif gyro.angle() < 180:
        turn_robot('right', gyro, left_motor, right_motor, 180)
    target_angle = 180
  #ev3.speaker.beep()
  # Checks if robot is in the right angle
  if gyro.angle() != target_angle:
    correct_direction(gyro, left_motor, right_motor, target_angle)


  #print("robot moves forward...")
  # Robot moves half a square on the grid. It then checks if its still @ the right
  # orientation. If not, it'll correct itself before moving forward another half square

  forward_robot(left_motor, right_motor)
  if gyro.angle() != target_angle:
    correct_direction(gyro, left_motor, right_motor, target_angle)
  forward_robot(left_motor, right_motor)
  if gyro.angle() != target_angle:
    correct_direction(gyro, left_motor, right_motor, target_angle)
  
  #print("End of instruction: " + str(gyro.angle()))
