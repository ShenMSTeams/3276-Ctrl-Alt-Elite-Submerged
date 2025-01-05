from hub import light_matrix
from hub import port
import runloop
import motor
import motor_pair
import math
from hub import motion_sensor


#######################
# advanced driving base
#######################
# robot wheel diameter
#wheel_dia = 86.9
#wheel_base = 142

#######################
# new design
#######################
# robot wheel diameter
wheel_dia = 56.5
wheel_base = 104

use_gyro = False
#use_gyro = True
min_velocity = 100
max_velocity = 360
max_ang_velocity = 100


def limit_range(value, min_val, max_val):
    """
    Limit `value` to lie between `min_val` and `max_val`
    """
    return min(max_val, max(min_val, value))


def get_yaw():
    """
    Get yaw angle, but try to correct for errors
    """
    global avg_yaw
    yaw = motion_sensor.tilt_angles()[0]
    return yaw


async def straight(dist, velocity=max_velocity, acceleration=500):
    """
    Move straight for dist mm
    """
    if use_gyro:
        await straight_gyro(dist, velocity=velocity, acceleration=acceleration)
    else:
        degrees = int(dist / (math.pi * wheel_dia) * 360)
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, degrees, 0, velocity=velocity, acceleration=acceleration, deceleration=acceleration)


async def turn(angle, velocity=max_ang_velocity, acceleration=1000):
    """
    turn angle in degrees
    """
    vel = int(velocity * wheel_base / wheel_dia)
    accel = int(acceleration * wheel_base / wheel_dia)
    if use_gyro:
        await turn_gyro(angle, velocity=vel)
    else:
        degrees = int(angle * wheel_base / wheel_dia)
        await motor_pair.move_for_degrees(motor_pair.PAIR_1, -degrees, 100, velocity=vel, acceleration=accel, deceleration=accel)


def yaw_at_angle(angle, velocity=max_ang_velocity):
    yaw = get_yaw()
    angle_error = yaw - angle * 10
    if abs(angle_error) < 10:
        motor_pair.stop(motor_pair.PAIR_1, stop=motor.BRAKE)
        print("end")
        return True
    
    #print (yaw, angle*10)
    vel = max(min_velocity, min(velocity,abs(angle_error)))
    if angle_error > 0:
        motor_pair.move(motor_pair.PAIR_1, 100, velocity=vel)
    else:
        motor_pair.move(motor_pair.PAIR_1, -100, velocity=vel)
    return False


async def turn_gyro(angle, velocity=max_ang_velocity):
    """
    turn angle in degrees using gyro
    """
    motor_pair.stop(motor_pair.PAIR_1, stop=motor.BRAKE)
    motion_sensor.reset_yaw(0)
    while motion_sensor.tilt_angles()[0] > 1:
        print('wait', motion_sensor.tilt_angles()[0])
    print ('start', motion_sensor.tilt_angles()[0])
    await runloop.until(lambda : yaw_at_angle(angle, velocity) )


async def straight_gyro(dist, velocity=max_velocity, acceleration=500):
    """
    drive straight and use gyro to correct direction
    """
    #stop the motors and reset the yaw angle
    motor_pair.stop(motor_pair.PAIR_1, stop=motor.BRAKE)
    motion_sensor.reset_yaw(0)

    # use positive dishtance but remember it's going backwards
    backward=False
    if dist < 0:
        dist=-dist
        backward=True

    # compute the target number of motor degrees to travel `dist`
    tgt_degrees = int(dist / (math.pi * wheel_dia) * 360)
    # reset the motor angle counters to zero
    motor.reset_relative_position(port.A, 0)
    motor.reset_relative_position(port.E, 0)

    # drive while correcting the steering
    while True:
        #adjust steering based on gyro yaw angle 
        yaw = get_yaw()
        if abs(yaw) > 200:
            print ("big yaw", yaw)
            #yaw=0
        steering = limit_range(yaw//10, -100, 100)

        
        avg_degrees = (abs(motor.relative_position(port.A)) + abs(motor.relative_position(port.E)))//2
        adj_velocity = acceleration*(tgt_degrees - avg_degrees)//250 + min_velocity
        adj_velocity = limit_range(adj_velocity, min_velocity, velocity)
        if backward:
            adj_velocity=-adj_velocity
            steering=-steering
        #print(steering, adj_velocity)
        motor_pair.move(motor_pair.PAIR_1, steering, velocity=adj_velocity)
        if avg_degrees > tgt_degrees:
            break
    motor_pair.stop(motor_pair.PAIR_1, stop=motor.BRAKE)
    await runloop.until(lambda: True)

###########################################################################

async def drive_square(size):
    '''
    drive in a square of size mm
    '''
    for i in range(4):
        await straight(size)
        await turn(90)


async def red_1_test():
    """
    shark tag  nursery water sample 
    """
    await straight(730)
    await turn(48)
    await straight(100)
    await straight(-260)
    await turn(90)
    await straight(500)
    

async def red_1():
    """or
    shark tag nursery water sample 
    """
    await straight(400)
    await turn(-25, velocity=50)
    await straight(350)
    await turn(115)
    await straight(190, acceleration= 1000, velocity= 1200)
    #arrived at coral on to shark
    await straight(-90)
    await turn(-45)
    await straight(220)
    #hit shark and return to base
    await straight(-200)
    await turn(120)
    await straight(600, velocity=1200)


async def red_2():
    """
    raise the mast going to blue base
    """
    await straight(420) 
    await turn(-95)
    await straight(330)
    await straight(70)
    await turn(-10)
    await straight(40)
    await straight (-70)
    await turn (-45)
    await straight (150)
    await turn (50)
    await straight (700, velocity=1200)
    await turn (-45)
    await straight (300, velocity=1200)


async def blue_5():
    """
    back up for unexpected encounter
    """
    await straight(190)
    await turn(-135)
    await straight (-450)
    #caught the octopus
    await straight(430, velocity=1200)


async def blue_6 ():
    """
    drop octopus off do angler fish
    """
    await straight (30)
    await turn (45)
    await straight (800)
    await turn (-45)  
    #octopus dropped off
    await straight (-90)
    await turn (46)
    await straight (250)
    await turn (30)
    await turn (-30)
    #angler fish done
    await straight (-400)
    await turn (30)
    await straight (-600, velocity=1200)


async def blue_7 ():
    """
    send over the submersable
    """
    await straight(430)
    await turn(47.5)
    await straight(700)
    await straight(100, acceleration=1500, velocity=600)
    await straight(-600)
    await turn(-30)
    await straight(-600)


async def main():
    #set up the driving motor pair
    motor_pair.unpair(motor_pair.PAIR_1)
    motor_pair.pair(motor_pair.PAIR_1, port.A, port.E)
    motion_sensor.set_yaw_face(motion_sensor.FRONT)
   # await drive_square(300)

    #await red_1 ()
    #await red_2() 
    #await blue_5() 
    await blue_6 ()
    #await blue_7 ()

runloop.run(main())
