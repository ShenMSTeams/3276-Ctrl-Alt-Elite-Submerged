from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, hub_menu, run_task, StopWatch

hub = PrimeHub()
hub.display.orientation(Side.RIGHT)

# Setup the robot drive base
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56.5, axle_track=104)
robot.settings(straight_speed=700)
default_settings = robot.settings()
robot.use_gyro(True)
print (default_settings)

# Setup the arm motor
arm_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE, gears=[20, 12, 36, 36])

def reset_drive():
    """
    Reset the robot drive base to the default speed and acceleration
    """
    robot.settings(*default_settings)

async def red_1():
    """
    shark, coral nursery, water sample, scuba divert, coeal reef
    """
    #await robot.straight(400)
    #return=
    await arm_motor.run_target (target_angle=90, speed=300)
    print("red 1")
    #hits water sample
    await robot.straight(480)
    #turns to go to go to seabed sample
    robot.settings(turn_rate=50)
    await robot.turn(47)
    await arm_motor.run_target (target_angle=0, speed=300)
    reset_drive()
    #go straight to seabed sample
    await robot.straight(575) 
    #arrived at sample getting ready to lift
    await arm_motor.run_target (target_angle=30, speed=300)
    #lifted up sample
    await robot.turn(30)
    await arm_motor.run_target (target_angle=-20, speed=300)
    #Dropped sample and heading to coral nursery
    await robot.straight(-40)
    await arm_motor.run_target (target_angle=0, speed=300)
    await robot.turn(-30)
    await robot.straight(-350)
    await robot.turn(-135)

    robot.settings(straight_acceleration=1000, straight_speed=300)
    await arm_motor.run_target (target_angle=15, speed=300)
    #pushing in the coral buds 
    await robot.straight(180)
    reset_drive()

    #lift the scuba diver
    await arm_motor.run_target (target_angle=30, speed=300)
    

    #backing up from coral nursery
    await robot.straight(-230)
    #turn to corral reef
    robot.settings(turn_rate=50)
    await robot.turn (90)
    reset_drive()
    #delivering scuba diver
    await robot.straight(50)
    await arm_motor.run_target (target_angle=12, speed=300)
    await robot.straight(-80)
    #released scuba diver
    await arm_motor.run_target(target_angle=-5, speed=300)
    await robot.straight(80)
    #flipping coral
    await robot.turn(7)
    await arm_motor.run_target(target_angle=-45, speed=300)
    await wait(500)
    await arm_motor.run_target(target_angle=-10, speed=300)
    await robot.turn(-7)
    #backing away from coral and alinging for raise the mast
    await robot.straight(-40)
    await robot.turn(45)
    await robot.straight(-50)
    #dropping arm to hook onto ship 
    await arm_motor.run_target(target_angle=-30, speed=300)
    await robot.turn(45)
    # raise the mast
    await robot.straight(100)

    await arm_motor.run_target(target_angle=30, speed=100)
    await robot.straight(-170)
    await arm_motor.run_target(target_angle=10, speed=300)
    #turns to get shark
    await robot.turn(-45)
    await arm_motor.run_target(target_angle=90, speed=300)
    await robot.turn(-90)
    

    
    #await robot.turn(-45)
    #await arm_motor.run_target(target_angle=90, speed=300)
    await robot.straight(300)
    #hit shark and return to base

    await robot.straight(-200)
    await robot.turn(-120)
    
    robot.settings(straight_speed=500)
    await robot.straight(700)
    reset_drive()
    await arm_mortar.run_target(target_angle=-45)

async def zero_arm():
    '''
    calibrating the arm attachment
    '''
    await arm_motor.run_until_stalled(speed=300, duty_limit=30)
    arm_motor.reset_angle(120)
    await arm_motor.run_target (target_angle=90, speed=300)
    return
    
async def red_2():
    """
    raise the mast going to blue base
    """ 
    await zero_arm()
    #trapping the shark
    await arm_motor.run_target(target_angle=-45, speed=300)
    await wait(1500)
    #raise the mast
    await robot.straight(400) 
    robot.settings(turn_rate=70,straight_speed=200)
    await robot.turn(90)
    await robot.straight(330)
    reset_drive()
    #await wait(1000)
    #delivering the shark
    await robot.straight(70)
    await robot.turn(45)
    await robot.straight(250)
    await robot.turn(-115)
    await robot.straight(30)
    await arm_motor.run_target(target_angle=90, speed=300)
    await robot.straight(-90)
    await arm_motor.run_target(target_angle=-45,speed=300)
    await robot.straight(100)
    await robot.straight(-90)
    #pulling the trident out
    await arm_motor.run_target(target_angle=90, speed=300)
    await robot.turn(-10)
    await robot.straight(110)
   # await robot.straight(-60)
    #await robot.turn(-45)
    await arm_motor.run_target (target_angle=0, speed=300)
    robot.settings(straight_speed=900,straight_acceleration=1550)
    await robot.straight(-130)
    reset_drive()
    await robot.straight(60)

    #await robot.turn(45)
    #await robot.straight(150)
    #await robot.turn(-60)

    #heading to blue base
    await robot.turn(85)
    robot.settings(straight_speed=500)
    await robot.straight(950)
    await robot.turn(45)
    await robot.straight(100)
    reset_drive()

async def red_3():
    '''
    research vesal
    '''
   # await robot.straight (600)
   ## robot.settings(straight_speed=100)
   # await robot.straight (770)
   # robot.settings(straight_speed=400)
    #await robot.straight (-1370)
    #await robot.turn (45)
    #await robot.straight (100)
    #await robot.turn (180)
    #await straight (200)
    #pushing the boat half way
    await robot.straight (530)
    robot.settings (straight_speed=200)
    await robot.straight (420)
    #curving and pushing the rest of the way
    await robot.curve(-90, 180)
    await robot.straight (-270)
    reset_drive()
    # returning too base
    await robot.straight (270)
    await robot.curve(90, 180)


async def blue_5():
    """
    back up for unexpected encounter
    """
    await arm_motor.run_target(target_angle=-45, speed=300)
    #line up with the mission
    robot.settings(straight_speed=200)
    await robot.straight(190)
    await robot.turn(135)
    #backing into it
    await robot.straight(-450)
    #caught the octopus now returning to base
    robot.settings(straight_speed=500)
    await robot.straight(430)
    reset_drive()


async def blue_6 ():
    """
    drop octopus off do angler fish
    """
    await zero_arm()
    # trapping the unknown creature
    await arm_motor.run_target(target_angle=-45, speed=300)
    #moving to deliver the unexpected
    await robot.straight(110)

    #robot.settings(turn_rate=50)
    await robot.turn(-50)
    #reset_drive()

    await robot.straight(620)
    await robot.turn(50)
    await robot.straight(120)

    await arm_motor.run_target(target_angle=0, speed=300)
    await robot.straight(-70)
    await robot.turn(-50)

    await arm_motor.run_target(target_angle=-45, speed=300)
    #octopus dropped off
    await robot.straight(160)
    await robot.turn(-35)
    await robot.turn(35)
    #angler fish done now back to base
    #await robot.straight(-380)
    #await robot.turn(-30)

    robot.settings(straight_speed=500)
    await robot.straight(-600)
    reset_drive()


async def blue_7 ():
    """
    send over the submersable and change shioping lanes
    """
    await arm_motor.run_target(target_angle=-45,speed=300) 
    await robot.curve(radius=2800, angle=-10)
    await robot.turn(60)
    await robot.straight(25)
    await arm_motor.run_target(target_angle=15, speed=300)
    await robot.turn(40)
    await robot.turn(-135)
    await arm_motor.run_target(target_angle=-10, speed=300)
    #await robot.straight(430)
    #await robot.turn(-45)
    await robot.straight(620)
    await arm_motor.run_target(target_angle=35, speed=300)
    await wait (2000)
    await arm_motor.run_target(target_angle=0, speed=300)

    #robot.settings(straight_speed=500, straight_acceleration=1000)
    #await robot.straight(100)
    #reset_drive()
    robot.settings(straight_speed=200)
    await robot.curve(radius=-200, angle=45, then=Stop.NONE)
    await robot.curve(radius=-200, angle=-45, then=Stop.NONE)
    await robot.straight(-300, then=Stop.NONE)
    await robot.curve(radius=-200, angle=-40, then=Stop.NONE)
    reset_drive()
    await robot.straight(-500)
    return

async def blue_8():
    '''
    change shiping lanes
    '''
    await arm_motor.run_target(target_angle=-45,speed=300) 
    await robot.curve(radius=2700, angle=-10)
    await robot.turn(60)
    await robot.straight(35)
    await arm_motor.run_target(target_angle=15, speed=300)
    await robot.turn(130)
    await robot.straight(300)

async def blue_9():
    '''
    artificial habitat
    '''
    #await arm_motor.run_target(target_angle=-20, speed=300)
    #await wait (1000)
    #arm_motor.run_target(target_angle=90, speed=2000)
    #await robot.straight(50)
    await robot.straight(170)
    await robot.turn(-90)
    await robot.straight(230)
    await arm_motor.run_target(target_angle=-10, speed=300)
    await robot.turn(45)
    await robot.straight(150)
    await arm_motor.run_target(target_angle=30, speed=300)
    await robot.straight(-130)
    await robot.turn(-45)
    await robot.straight(-50)
    await arm_motor.run_target(target_angle=-20, speed=300)
    await robot.straight(70)
    await robot.turn(45)
    await robot.turn(-45)
    await robot.straight(60)
    await robot.straight(-15)
    await arm_motor.run_target(target_angle=90, speed=1000)

    
async def calibrate_arm():
    """
    Adjust the angle of the arm to use as zero degrees

    Pressing the left/right buttons changes the arm by one degree
    Pressing and holding the buttons scans through angles quickly after
    a one second delay
    """
    # reset the current motor angle to be zero degrees
    arm_motor.reset_angle(0)
    a=0
    hub.display.number(a)
    clock = StopWatch()
    # how long to wait while holding a button before counting additional presses
    delay = 1000
    # indicate if a button press has been handled yet
    handled = False
    while True:
        # check if any buttons are pressed
        pressed = hub.buttons.pressed()
        # handle a button press if not already handled or if the time delay has passed
        if pressed and not handled or clock.time() > delay:
            if Button.RIGHT in pressed:
                a = a + 1
            if Button.LEFT in pressed:
                a = a - 1
            if Button.BLUETOOTH in pressed:
                break
            # mark the button press as handled so we don't repeat it
            handled = True
            # adjust the motor angle and display
            hub.display.number(a)
            arm_motor.track_target(target_angle=a)

        # after the delay has occured while holding a button reset the clock
        # also make the delay very small to allow quickly scanning angles
        if pressed and clock.time() > delay:
            clock.reset()
            delay = 10

        # if the button has been released then reset the handled flag,
        # reset the clock, and reset to a long delay
        if not pressed:
            handled = False
            clock.reset()
            delay = 1000

    # reset the current motor angle to be zero degrees
    arm_motor.reset_angle(0)



# Dictionary of all runs and their display character
runs = {"1" : red_1, 
        "2" : red_2,
        "3" : red_3,
        "5" : blue_5,
        "6" : blue_6,
        "7" : blue_7,
        "8" : blue_8,
        "9" : blue_9,
        "0" : zero_arm,
        "C" : calibrate_arm}


def stop_motors():
    """
    Stop all motors
    """
    left_motor.stop()
    right_motor.stop()
    arm_motor.stop()


def main():
    print("battery voltage: ", hub.battery.voltage(), "mV")
    print("battery current: ", hub.battery.current(), "mA")

    #wait for IMU to calibrate
    hub.display.icon(Icon.EMPTY)
    while not hub.imu.ready():
        None

    run_keys = sorted(runs.keys())
    n = 0
    while True:
        # rotate the keys to start with the nth item
        rotated_keys = run_keys[n:] + run_keys[:n]
        # Get the user selection on which run to launch
        selection = hub_menu(*rotated_keys)
        # get the index of the selected key in the original list
        n = run_keys.index(selection)
        # move index to the next item to run, modulo number of keys
        n = (n + 1) % len(run_keys)
    
        # Launch the selected run
        if selection in runs.keys():
            hub.display.icon(Icon.ARROW_UP)
            run_task(runs[selection]())
            stop_motors()


main()
