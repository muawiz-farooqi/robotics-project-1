from pybricks.parameters import Port, Stop, Direction, Button, Color

#run_target(speed, target_angle, then=Stop.HOLD, wait=True)
def forward_robot(left_motor, right_motor):

  print(left_motor.angle())
  print(right_motor.angle())
  left_motor.run(25)
  right_motor.run(25)

  while True:
    left_motor.run_target(25,720)
    right_motor.run_target(25,720)
    break
