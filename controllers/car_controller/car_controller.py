from controller import Robot, Motor

TIME_STEP = 64
robot = Robot()
ds = []
dsNames = ['ds_right', 'ds_right(1)', 'ds_right(2)', 'ds_left', 'ds_left(1)', 'ds_left(2)']
rotations = []
rotName = ['fl_rot_motor', 'fr_rot_motor']
for i in range(6):
    ds.append(robot.getDevice(dsNames[i]))
    ds[i].enable(TIME_STEP)
for i in range(2):
    rotations.append(Motor(rotName[i]))
    rotations[i].setVelocity(0.5)
wheels = []
wheelsNames = ['wheel1', 'wheel2', 'wheel3', 'wheel4']
for i in range(4):
    wheels.append(robot.getDevice(wheelsNames[i]))
    wheels[i].setPosition(float('inf'))
    wheels[i].setVelocity(0.0)
avoidObstacleCounter = 0
MAX_SPEED = 6.28
k = 0.15
f = 0

while robot.step(TIME_STEP) != -1:
    right_obstacle = ds[0].getValue() < 950 or ds[1].getValue() < 900 or ds[2].getValue() < 850
    left_obstacle = ds[3].getValue() < 950 or ds[4].getValue() < 900 or ds[5].getValue() < 850


    # leftSpeed = 1.0
    # rightSpeed = 1.0
    # if f:
    #     f = 0
    #     rotations[0].setPosition(-f)
    #     rotations[1].setPosition(-f)
    # fleftSpeed = k * MAX_SPEED
    # frightSpeed = k * MAX_SPEED
    # leftSpeed = rightSpeed = fleftSpeed
    # if avoidObstacleCounter > 0:
    #     avoidObstacleCounter -= 1
    #     # leftSpeed = 1.0
    #     # rightSpeed = -1.0
    #     f = 0.8
    #     rotations[0].setPosition(f)
    #     rotations[1].setPosition(f)
    #     fleftSpeed = k * MAX_SPEED
    #     frightSpeed = MAX_SPEED
    #     leftSpeed = 0
    #     rightSpeed = MAX_SPEED
    # else:  # read sensors
    #     for i in range(6):
    #         if ds[i].getValue() < 950.0:
    #             avoidObstacleCounter = 100

    # инициализировать скорость двигателя на k от MAX_SPEED.
    if right_obstacle:
        # Поворот налево
        f = 0.8
        rotations[0].setPosition(f)
        rotations[1].setPosition(f)
        fleftSpeed = k * MAX_SPEED
        frightSpeed = MAX_SPEED
        leftSpeed = 0
        rightSpeed = MAX_SPEED

    elif left_obstacle:
        # Поворот направо
        f = -0.8
        rotations[0].setPosition(f)
        rotations[1].setPosition(f)
        fleftSpeed = MAX_SPEED
        frightSpeed = k * MAX_SPEED
        leftSpeed = MAX_SPEED
        rightSpeed = 0
    else:
        if f:
            f = 0
            rotations[0].setPosition(-f)
            rotations[1].setPosition(-f)
        fleftSpeed = k * 2 * MAX_SPEED
        frightSpeed = k * 2 * MAX_SPEED
        leftSpeed = rightSpeed = fleftSpeed
    # запись входов исполнительных механизмов
    wheels[0].setVelocity(fleftSpeed)
    wheels[1].setVelocity(frightSpeed)
    wheels[2].setVelocity(leftSpeed)
    wheels[3].setVelocity(rightSpeed)
