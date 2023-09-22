#!/bin/bash

dunst &
xdg-user-dirs-update &
feh --randomize --bg-fill /home/dmne/Pictures/background &
#nitrogen --restore &
#picom -f &
#picom &
picom --experimental-backend &
#blueberry-tray &
#blueman-applet &
#pasystray --notify=all instead &
pasystray &
nm-applet &
#gammy &
# syncthing &
# mpd &
#volumeicon & 
#cbatticon &
#variety &
#parcellite &
/usr/bin/lxpolkit &
dbus-update-activation-environment --systemd DBUS_SESSION_BUS_ADDRESS DISPLAY XAUTHORITY &

