from pybricks.parameters import Port, Stop, Direction, Button, Color

#run_target(speed, target_angle, then=Stop.HOLD, wait=True)
def forward_robot(left_motor, right_motor):
  wheel_diam = 6.8 # cm 
  wheel_turn = 360 * (15.25 / (wheel_diam * 3.1415927)) 
  while True:
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.run_target(50, wheel_turn, then=Stop.BRAKE, wait=False)
    right_motor.run_target(50,wheel_turn, then=Stop.BRAKE, wait=True)
    break
