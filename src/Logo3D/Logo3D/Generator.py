###############################################
# Libraries
###############################################

import sys
import os

from Parser import *
from Turtle3D import Turtle3D

###############################################
# generate_moves()
###############################################

def generate_moves(tokens, index, all_pos_sequences, current_pos_sequence, turtle, debug_mode):
    while(index < len(tokens)):
        token = tokens[index]
        if (not (isinstance(token, tuple))):
            command = token
            if (command == PENUP):
                turtle.pendown = False
                all_pos_sequences.append(current_pos_sequence)
                current_pos_sequence = []
            elif (command == PENDOWN):
                turtle.pendown = True
            elif (command == HOME):
                turtle.x = 0
                turtle.y = 0
                turtle.horizontal_angle = 0
                turtle.vertical_angle = 0
        elif len(token) == 2:
            (command, param) = token
            if (command not in [FORWARD, BACKWARD, RIGHT_TURN, LEFT_TURN, UP_TURN, DOWN_TURN]):
                printf(f"ERROR: Unexpected command: {command} (should be {FORWARD}, {BACKWARD}, {RIGHT_TURN}, {LEFT_TURN}, {RIGHT_TURN}, {LEFT_TURN}, {UP_TURN} or {DOWN_TURN} for {FD_STR}, {BK_STR}, {RT_STR}, {LT_STR}, {UT_STR} or{DT_STR},")
                os._exit(1)

            if (command == FORWARD):
                (x1, y1, z1) = (turtle.x, turtle.y, turtle.z)
                turtle.move(param)
                (x2, y2, z2) = (turtle.x, turtle.y, turtle.z)

                if (turtle.pendown):
                    current_pos_sequence.append((x1, y1, z1))
                    current_pos_sequence.append((x2, y2, z2))
            elif (command == BACKWARD):
                (x1, y1, z1) = (turtle.x, turtle.y, turtle.z)
                turtle.move(-param)
                (x2, y2, z2) = (turtle.x, turtle.y, turtle.z)

                if (turtle.pendown):
                    current_pos_sequence.append((x1, y1, z1))
                    current_pos_sequence.append((x2, y2, z2))
            elif (command == RIGHT_TURN):
                turtle.horizontal_turn(param)
            elif (command == LEFT_TURN):
                turtle.horizontal_turn(-param)
            elif (command == UP_TURN):
                turtle.vertical_turn(param)
            elif (command == DOWN_TURN):
                turtle.vertical_turn(-param)
            else:
                print("NOT YET IMPLEMENTED!")
                os._exit(1)

        elif len(token) == 3:
            (command, repeat_count, sub_commands) = token
            if (command != REPEAT):
                printf(f"ERROR: Unexpected command: {command} (should be {REPEAT} for {REPEAT_STR})")
                os._exit(1)
            while (repeat_count > 0):
                generate_moves(sub_commands, 0, all_pos_sequences, current_pos_sequence, turtle, debug_mode)
                repeat_count -= 1
        else:
            printf(f"ERROR: Unexpected token: {token}")
            os._exit(1)
        index += 1

###############################################
# generate()
###############################################

def generate(tokens, debug_mode):
    turtle = Turtle3D()
    all_pos_sequences = []
    current_pos_sequence = []
    generate_moves(tokens, 0, all_pos_sequences, current_pos_sequence, turtle, debug_mode)
    all_pos_sequences.append(current_pos_sequence)
    
    if (debug_mode):
        print("Generating...")
        print(all_pos_sequences)
        print()
    return all_pos_sequences

