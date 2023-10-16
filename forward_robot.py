from pybricks.parameters import Port, Stop, Direction, Button, Color

#run_target(speed, target_angle, then=Stop.HOLD, wait=True)
def forward_robot(left_motor, right_motor):

  print(left_motor.angle())
  print(right_motor.angle())

  while True:
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    left_motor.run_target(25,720, then=Stop.BRAKE, wait=False)
    right_motor.run_target(25,720, then=Stop.BRAKE, wait=True)
    break
