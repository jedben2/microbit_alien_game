# So far: spawns alien at some direction. if point towards it flashes an alien picture
# if press A then shoot and new alien appear (make kill and points award)
# if time out (5 seconds) them X appear (make new round happen)
# need make number of rounds and then total points. maube highscore perhaps not since is prototype

from microbit import *

compass_directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

def get_compass_direction(heading):
    # heading = input.compass_heading()
    if heading + 22.5 >= 360: heading -= 360
    return compass_directions[(heading + 22.5) // 45]

def draw_alien():
    basic.show_leds("""
        . # # # .
        # . # . #
        # # # # #
        . # . # .
        # # . # #
        """)

def main():
    playing = True
    while playing:
        alien = randint(0, 360) + 180
        if alien > 360: alien -= 360
        if input.button_is_pressed(Button.AB):
            playing = False
            basic.show_string("bye")
            break
        basic.show_string(get_compass_direction(alien))
        t1 = input.running_time()
        while not input.button_is_pressed(Button.A):
            if 22.5 <= alien < 337.5:
                if alien - 22.5 < input.compass_heading() < alien + 22.5:
                    draw_alien()
                else: 
                    basic.show_number(int(5 - (input.running_time() - t1) // 1000), 1)
            elif alien > 375.5:
                if alien - 22.5 < input.compass_heading() or 22.5 - 360 + alien > input.compass_heading():
                    draw_alien()
                else: 
                    basic.show_number(int(5 - (input.running_time() - t1) // 1000), 1)
            else:
                if alien - 22.5 + 360 < input.compass_heading() or alien + 22.5 > input.compass_heading():
                    draw_alien()
                else:
                    basic.show_number(int(5 - (input.running_time() - t1) // 1000), 1)
            if input.running_time() - t1 > 6000:
                basic.show_leds("""
                # . . . #
                . # . # .
                . . # . .
                . # . # .
                # . . . #
                """)
                pause(2000)
        basic.clear_screen()

main()
