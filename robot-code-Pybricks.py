from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Icon
from pybricks.robotics import DriveBase
from pybricks.tools import wait, hub_menu, run_task

hub = PrimeHub()

# Setup the robot drive base
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.E, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56.5, axle_track=104)
robot.settings(straight_speed=700)
default_settings = robot.settings()
robot.use_gyro(True)


def reset_drive():
    """
    Reset the robot drive base to the default speed and acceleration
    """
    robot.settings(*default_settings)


async def red_1():
    """
    shark tag nursery water sample 
    """
    print("red 1")
    await robot.straight(400)

    robot.settings(turn_rate=50)
    await robot.turn(25)
    reset_drive()

    await robot.straight(350)
    await robot.turn(-115)

    robot.settings(straight_acceleration=1000, straight_speed=500) 
    await robot.straight(200)
    reset_drive()

    #arrived at coral on to shark
    await robot.straight(-90)
    await robot.turn(40)
    await robot.straight(220)
    #hit shark and return to base
    await robot.straight(-200)
    await robot.turn(-120)
    
    robot.settings(straight_speed=500)
    await robot.straight(600)
    reset_drive()

    
async def red_2():
    """
    raise the mast going to blue base
    """
    await robot.straight(420) 
    await robot.turn(95)
    await robot.straight(330)
    await wait(1000)
    await robot.straight(70)
    await robot.turn(10)
    await robot.straight(40)
    await robot.straight(-70)
    await robot.turn(45)
    await robot.straight(150)
    await robot.turn(-60)

    robot.settings(straight_speed=500)
    await robot.straight(700)
    await robot.turn(45)
    await robot.straight(300)
    reset_drive()


async def blue_5():
    """
    back up for unexpected encounter
    """
    await robot.straight(190)
    await robot.turn(135)
    await robot.straight(-450)
    #caught the octopus
    robot.settings(straight_speed=500)
    await robot.straight(430)
    reset_drive()


async def blue_6 ():
    """
    drop octopus off do angler fish
    """
    await robot.straight(110)

    robot.settings(turn_rate=50)
    await robot.turn(-50)
    reset_drive()

    await robot.straight(600)
    await robot.turn(50)
    await robot.straight(80)
    await robot.straight(-60)
    await robot.turn(-48)
    #octopus dropped off
    await robot.straight(260)
    await robot.turn(-35)
    await robot.turn(30)
    #angler fish done
    #await robot.straight(-380)
    #await robot.turn(-30)

    robot.settings(straight_speed=500)
    await robot.straight(-1000)
    reset_drive()


async def blue_7 ():
    """
    send over the submersable
    """
    await robot.straight(430)
    await robot.turn(-47.5)
    await robot.straight(700)

    robot.settings(straight_speed=500, straight_acceleration=1000)
    await robot.straight(100)
    reset_drive()

    await robot.straight(-600)
    await robot.turn(30)
    await robot.straight(-600)


# Dictionary of all runs and their display character
runs = {"1" : red_1, 
        "2" : red_2,
        "5" : blue_5,
        "6" : blue_6,
        "7" : blue_7}


def stop_motors():
    """
    Stop all motors
    """
    left_motor.stop()
    right_motor.stop()


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