
# Function for turning the robot 90 degrees
def turn_robot(direction, gyro, left_motor, right_motor, target_angle):
  print("turn robot called " + direction + " " + str(target_angle))
  gyro_curr_angle = gyro.angle()
  #run_angle(speed, rotation_angle, then=Stop.HOLD, wait=True)
  if direction == 'left':
    while gyro.angle() > target_angle:
      left_motor.run(-100)
      right_motor.run(100)
    left_motor.brake()
    right_motor.brake()
  elif direction == 'right':
    while gyro.angle() < target_angle:
      left_motor.run(100)
      right_motor.run(-100)
    left_motor.brake()
    right_motor.brake()

  if(gyro.angle() != target_angle):
    correct_direction(gyro, left_motor, right_motor, target_angle)
  

def correct_direction(gyro, left_motor, right_motor, target_angle):
  #print("correct_direction called: " + str(gyro.angle()) + " " + str(target_angle))
  gyro_curr_angle = gyro.angle()
  if gyro.angle() > target_angle:
    while gyro.angle() > target_angle:
      right_motor.run(25)
    left_motor.brake()
    right_motor.brake()
  elif gyro.angle() < target_angle:
    while gyro.angle() < target_angle:
      left_motor.run(25)
    left_motor.brake()
    right_motor.brake()
  if gyro.angle() != target_angle:
    correct_direction(gyro, left_motor, right_motor, target_angle)