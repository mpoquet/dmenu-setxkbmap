#!/usr/bin/env python3
"""A dmenu setxkbmap wrapper."""

import os
import subprocess
import re
import sys

def current_layout():
    """Gets the current layout (as LAYOUT[ VARIANT])."""
    code, output = subprocess.getstatusoutput("setxkbmap -query")
    if code != 0:
        raise Exception("'setxkbmap -query' failed")

    match_layout = re.search(r"layout:\s+(\S+)", output)
    if match_layout:
        layout = match_layout.group(1)
    else:
        raise Exception("Cannot retrieve layout in setxkbmap -query result")

    match_variant = re.search(r"variant:\s+(\S+)", output)
    if match_variant:
        variant = match_variant.group(1)
        return '{layout} {variant}'.format(layout=layout, variant=variant)

    return layout

def default_x11_layouts():
    """Gets system's default layouts."""
    code, output = subprocess.getstatusoutput(
        "localectl list-x11-keymap-layouts")
    if code != 0:
        raise Exception("localectl list-x11-keymap-layouts failed")
    return output

def input_layouts():
    """ Retrieve script input layouts."""
    if "LAYOUTS" in os.environ:
        as_string = os.environ["LAYOUTS"]
    else:
        as_string = default_x11_layouts()

    return as_string.split('\n')

def swap_first_input_if_current(curr_layout, in_layouts):
    """ Swap first and second layouts if first layout is the current one."""
    layouts = list(in_layouts)
    if len(layouts) > 1:
        if layouts[0] == curr_layout:
            layouts[0], layouts[1] = layouts[1], layouts[0]
    return layouts

def dmenu_setxkbmap(force_space_keymap=True):
    """Script main function.

    1. Generate a dmenu input
    2. Call dmenu to ask user's choice
    3. Call setxkbmap on selected choice
    """
    # Generate the desired list of X11 layouts
    in_layouts = swap_first_input_if_current(current_layout(), input_layouts())
    layouts_as_str = '\n'.join(in_layouts).encode('utf-8')

    # Call dmenu on our lists of layouts
    proc = subprocess.run(['dmenu'] + sys.argv[1:],
                          input=layouts_as_str,
                          stdout=subprocess.PIPE)

    if proc.returncode == 0:
        choice = proc.stdout.decode('utf-8').strip()

        # Call setxkbmap on selected choice
        returncode, _ = subprocess.getstatusoutput('setxkbmap {layout}'.format(
            layout=choice))
        success = (returncode == 0)

        if success and force_space_keymap:
            # Force keymap of the space keycode
            code, _ = subprocess.getstatusoutput('xmodmap -e "keycode 65 = space space space space underscore underscore space space"')
            success = (code == 0)
    else:
        success = False

    return success

if __name__ == "__main__":
    if dmenu_setxkbmap():
        sys.exit(0)
    else:
        sys.exit(1)
