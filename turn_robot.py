
# Function for turning the robot 90 degrees
def turn_robot(direction, gyro, left_motor, right_motor):
  gyro_curr_angle = gyro.angle()
  #run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)
  if direction == 'left':
    while gyro.angle() > gyro_curr_angle - 90:
      left_motor.run(-100)
      right_motor.run(100)
    left_motor.brake()
    right_motor.brake()
  elif direction == 'right':
    while gyro.angle() < gyro_curr_angle + 90:
      left_motor.run(100)
      right_motor.run(-100)
    left_motor.brake()
    right_motor.brake()
