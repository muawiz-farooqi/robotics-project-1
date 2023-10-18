
# Function for turning the robot 90 degrees
def turn_robot(direction, gyro, left_motor, right_motor, target_angle):
  print("turn robot called " + direction + " " + str(target_angle))
  gyro_curr_angle = gyro.angle()
  #run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)
  if direction == 'left':
    while gyro.angle() > target_angle:
      left_motor.run(-85)
      right_motor.run(85)
    left_motor.brake()
    right_motor.brake()
  elif direction == 'right':
    while gyro.angle() < target_angle:
      left_motor.run(85)
      right_motor.run(-85)
    left_motor.brake()
    right_motor.brake()
