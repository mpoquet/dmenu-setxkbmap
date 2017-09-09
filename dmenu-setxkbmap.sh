#!/usr/bin/env bash

# The script will stop on dmenu error (user cancel)
set -e

# Default x11 layouts are listed if LAYOUTS is undefined
if [ -z "${LAYOUTS}" ]
then
    LAYOUTS=$(localectl list-x11-keymap-layouts)
fi

# Call dmenu and get the user selection
choice=$(echo "${LAYOUTS}" | dmenu "$@")
echo "Choice: #${choice}#"

# Finally call setxkbmap
setxkbmap ${choice}
