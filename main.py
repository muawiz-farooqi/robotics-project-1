#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from turn_robot import turn_robot
from forward_robot import forward_robot

import math
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
right_motor = Motor(Port.A)
left_motor = Motor(Port.D)
gyro = GyroSensor(Port.S2)


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
# #goal = [3.658, 1.829]
# #start = {0.305, 1.219};
# workspace = [[-1 for x in range(16)] for y in range(10)]

# workspace[math.ceil(1.829/0.305)][math.ceil(3.658/0.305)] = 0
# #workspace[math.ceil(1.219/0.305)][math.ceil(0.305/0.305)] = 0

# for obstacle in obstacles:
#   if obstacle[0] == -1:
#     continue
#   x = math.ceil(obstacle[0]/0.305)
#   y = math.ceil(obstacle[1]/0.305)
#   workspace[y][x] = 1000
# #print(obstacles)

# print(workspace)

# Write your program here.
ev3.speaker.beep()
gyro.reset_angle(0)
left_motor.reset_angle(0)
right_motor.reset_angle(0)

# turn_robot('left',gyro, left_motor, right_motor)
# turn_robot('right',gyro, left_motor, right_motor)
# turn_robot('left',gyro, left_motor, right_motor)
# turn_robot('right',gyro, left_motor, right_motor)

forward_robot(left_motor, right_motor)
