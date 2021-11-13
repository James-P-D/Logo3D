###############################################
# Libraries
###############################################

import sys
import os

###############################################
# Constants
###############################################

FD_STR = "FD"
BK_STR = "BK"
RT_STR = "RT"
LT_STR = "LT"
UT_STR = "UT"
DT_STR = "DT"
REPEAT_STR = "REPEAT"
OPEN_BRACKET_STR = "["
CLOSE_BRACKET_STR = "]"

FORWARD = 0
BACKWARD = 1
RIGHT_TURN = 2
LEFT_TURN = 3
UP_TURN = 4
DOWN_TURN = 5
REPEAT = 6

###############################################
# parse()
###############################################

def parse(tokens, debug_mode):
   
    ###############################################
    # parse()
    ###############################################

    def parse(tokens, index, open_bracket_count, debug_mode):
        commands = []
        while (index < len(tokens)):
            current_token = tokens[index]
            if (debug_mode):
                print(f"{current_token}")
            if (current_token in [FD_STR, BK_STR, RT_STR, LT_STR, UT_STR, DT_STR]):
                index += 1
                if (index == len(tokens)):
                    print(f"ERROR: Expected integer token after {current_token}")
                    os._exit(1)
                param_token = tokens[index]
                if (debug_mode):
                    print(f"{param_token}")

                try:
                    param_token_float = float(param_token)
                    if (current_token == FD_STR):
                        commands.append((FORWARD, param_token_float))
                    elif (current_token == BK_STR):
                        commands.append((BACKWARD, param_token_float))
                    elif (current_token == RT_STR):
                        commands.append((RIGHT_TURN, param_token_float))
                    elif (current_token == LT_STR):
                        commands.append((LEFT_TURN, param_token_float))
                    elif (current_token == UT_STR):
                        commands.append((UP_TURN, param_token_float))
                    elif (current_token == DT_STR):
                        commands.append((DOWN_TURN, param_token_float))
                    else:
                        # This shouldn't ever happen, but adding it incase we add to the 'in' list but forget to actual handle it
                        print(f"ERROR: {current_token} is not an expected token here")
                        os._exit(1)
                except:
                    print(f"ERROR: Expected a float after {current_token} but instead found {param_token}")
                    os._exit(1)
            elif (current_token == REPEAT_STR):
                index += 1
                if (index == len(tokens)):
                    print(f"ERROR: Expected integer token after {current_token}")
                    os._exit(1)
                param_token = tokens[index]
                if (debug_mode):
                    print(f"{param_token}")

                try:
                    param_token_int = int(param_token)
                    index += 1
                    if (index == len(tokens)):
                        print(f"ERROR: Expected {OPEN_BRACKET_STR} token after {current_token}")
                        os._exit(1)
                   
                    open_bracket_token = tokens[index]
                    if (debug_mode):
                        print(f"{open_bracket_token}")

                    if (open_bracket_token != OPEN_BRACKET_STR):
                        print(f"ERROR: Expected {OPEN_BRACKET_STR} token after {current_token}")
                        os._exit(1)

                    index += 1
                    open_bracket_count += 1
                    (repeat_commands, updated_index, new_open_bracket_count) = parse(tokens, index, open_bracket_count, debug_mode)
                    commands.append((REPEAT, param_token_int, repeat_commands))
                    index = updated_index
                    open_bracket_count = new_open_bracket_count

                except:
                    print(f"ERROR: Expected an int after {current_token} but instead found {param_token}")
                    os._exit(1)

            elif (current_token == CLOSE_BRACKET_STR):
                open_bracket_count -= 1
                if (open_bracket_count < 0):
                    print(f"ERROR: Unexpected {CLOSE_BRACKET_STR}")
                    os._exit(1)
                return (commands, index, open_bracket_count)
            else:
                print(f"ERROR: {current_token} is not an expected token here")
                os._exit(1)
            index += 1

        return (commands, index, open_bracket_count)

    
    if (debug_mode):
        print("Parsing")

    (commands, index, open_bracket_count) = parse(tokens, 0, 0, debug_mode)
    if (open_bracket_count != 0):
        print(f"ERROR: {new_open_bracket_count} remain unclosed at EOF")
        os._exit(1)
    if (index < len(tokens)):
        print(f"ERROR: Unprocessed tokens")
        os._exit(1)

    if (debug_mode):
        print(commands)
        print()
    return commands

