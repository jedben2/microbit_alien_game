from microbit import *

compass_directions = ["N", "NW", "W", "SW", "S", "SE", "E", "NE"]

def get_compass_direction():
    heading = input.compass_heading()
    if heading + 22.5 >= 360: heading -= 360
    return compass_directions[(heading + 22.5) // 45]

def main():
    playing = True
    while playing:
        if input.button_is_pressed(Button.AB):
            playing = False
            basic.show_string("bye")


main()
