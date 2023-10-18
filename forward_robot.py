from pybricks.parameters import Port, Stop, Direction, Button, Color

#run_target(speed, target_angle, then=Stop.HOLD, wait=True)
def forward_robot(left_motor, right_motor):
  while True:
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.run_target(25,680, then=Stop.BRAKE, wait=False)
    right_motor.run_target(25,680, then=Stop.BRAKE, wait=True)
    break
