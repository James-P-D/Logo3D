###############################################
# Libraries
###############################################

import sys
import os

from Parser import *
from Turtle3D import Turtle3D

###############################################
# generate()
###############################################

def generate(tokens, debug_mode):

    ###############################################
    # generate()
    ###############################################

    def generate_moves(tokens, index, turtle, debug_mode):
        positions = []

        while(index < len(tokens)):
            token = tokens[index]
            if len(token) == 2:
                (command, param) = token
                if (command not in [FORWARD, BACKWARD, RIGHT_TURN, LEFT_TURN, UP_TURN, DOWN_TURN]):
                    printf(f"ERROR: Unexpected command: {command} (should be {FORWARD}, {BACKWARD}, {RIGHT_TURN}, {LEFT_TURN}, {RIGHT_TURN}, {LEFT_TURN}, {UP_TURN} or {DOWN_TURN} for {FD_STR}, {BK_STR}, {RT_STR}, {LT_STR}, {UT_STR} or{DT_STR},")
                    os._exit(1)

                if (command == FORWARD):
                    (x1, y1, z1) = (turtle.x, turtle.y, turtle.z)
                    turtle.move(param)
                    (x2, y2, z2) = (turtle.x, turtle.y, turtle.z)
                    positions.append((x1, y1, z1))
                    positions.append((x2, y2, z2))
                elif (command == BACKWARD):
                    (x1, y1, z1) = (turtle.x, turtle.y, turtle.z)
                    turtle.move(-param)
                    (x2, y2, z2) = (turtle.x, turtle.y, turtle.z)
                    positions.append((x1, y1, z1))
                    positions.append((x2, y2, z2))
                elif (command == RIGHT_TURN):
                    turtle.turn(param)
                elif (command == LEFT_TURN):
                    turtle.turn(-param)
                else:
                    print("NOT YET IMPLEMENTED!")
                    os._exit(1)

            elif len(token) == 3:
                (command, repeat_count, sub_commands) = token
                if (command != REPEAT):
                    printf(f"ERROR: Unexpected command: {command} (should be {REPEAT} for {REPEAT_STR})")
                    os._exit(1)
                while (repeat_count > 0):
                    new_positions = generate_moves(sub_commands, 0, turtle, debug_mode)
                    positions = positions + new_positions
                    repeat_count -= 1
            else:
                printf(f"ERROR: Unexpected token: {token}")
                os._exit(1)
            index += 1

        return positions

    turtle = Turtle3D()

    positions = generate_moves(tokens, 0, turtle, debug_mode)
    
    if (debug_mode):
        print("Generating")
        print(positions)
        print()
    return positions

