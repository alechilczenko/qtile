from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal
import os


black = "#11111B"
gray = "#1E1E2E"
purple = "#cba6f7"
red = "#f38ba8"
green = "#a6e3a1"
blue = "#89b4fa"
white = "#cdd6f4"

screens = [
    Screen(
        top=bar.Bar(
            [   widget.Sep(padding=3, linewidth=0, background=gray),
                widget.Image(filename='/home/ale/.config/qtile/eos-c.png', margin=3, background=gray, mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")}),
                widget.Sep(padding=4, linewidth=0, background=gray), 
                widget.GroupBox(
                                highlight_method='block',
                                this_screen_border=white,
                                this_current_screen_border=black,
                                active="#FFFFFF",
                                inactive=white,
                                background=gray),  
                widget.Spacer(length=5),
                widget.WindowName(foreground=white,fmt='{}'),
                widget.CurrentLayoutIcon(scale=0.75),
                widget.Spacer(length=10),
                widget.Systray(icon_size = 20),
                volume,
                widget.Spacer(length=10),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p',
                             background=black,
                             foreground=purple),
                widget.TextBox(
                    text='Power Menu',
                    mouse_callbacks= {
                        'Button1':
                        lambda: qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh'))
                    },
                    foreground=green
                ),
                widget.Spacer(length=10)
            ],
            30,  # height in px
            background=black  # background color
        ), ),
]
