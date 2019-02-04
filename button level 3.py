#make a function that determines the angle the microbit is tilted at
import math
import microbit
#import time

def find_x_tilt(x, y, z):
    x_radians = math.atan2(x, (math.sqrt((y ** 2) + (z ** 2))))
    return x_radians

def find_y_tilt(x, y, z):
    y_radians = math.atan2(y, (math.sqrt((x ** 2) + (z ** 2))))
    return y_radians

#print(find_x_tilt(x, y, z))

#print(find_y_tilt(x, y, z))

def x_radians_to_degrees(x_r):
    x_degrees = math.degrees(x_r)
    return x_degrees

def y_radians_to_degrees(y_r):
    y_degrees = math.degrees(y_r)
    return y_degrees

def adjust(x1, y1):
    if ((x1<=-5 and x1>=-7) and (y1<=5 and y1>=-1)):
        microbit.display.show(microbit.Image.HAPPY)
    elif(x1>=-7 and y1<=-5):
        microbit.display.show(microbit.Image.ARROW_S)
    elif(x1>=0 and y1>=10):
        microbit.display.show(microbit.Image.ARROW_W)
    elif(x1>=-8 and y1>=6):
        microbit.display.show(microbit.Image.ARROW_N)
    elif(x1<=-20 and y1>=-1):
        microbit.display.show(microbit.Image.ARROW_E)

while True:
    x = microbit.accelerometer.get_x()
    y = microbit.accelerometer.get_y()
    z = microbit.accelerometer.get_z()
    microbit.sleep(100)



    x_r = find_x_tilt(x, y, z)
    y_r = find_y_tilt(x, y, z)

    print(x_radians_to_degrees(x_r))
    print(y_radians_to_degrees(y_r))


    x1 = x_radians_to_degrees(x_r)
    y1 = y_radians_to_degrees(y_r)

    adjust(x1, y1)



