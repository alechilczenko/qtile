#!/bin/sh

# Obtén la lista de dispositivos de salida
outputs=$(xrandr | grep " connected" | awk '{print $1}')

# Verifica si HDMI-1 está presente en la lista de dispositivos
if [[ $outputs == *"HDMI-1"* ]]; then
    # Establece HDMI-1 como pantalla principal
    xrandr --output HDMI-1 --primary --auto
    xrandr --output eDP-1 --off	
else
    xrandr --output eDP-1 --primary --auto
fi

feh --bg-fill $HOME/wallpapers/mountains.jpg

picom & disown # --experimental-backends --vsync should prevent screen tearing on most setups if needed

# Low battery notifier
~/.config/qtile/scripts/check_battery.sh & disown

# Start welcome
eos-welcome & disown

/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & disown # start polkit agent from GNOME
