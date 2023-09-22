# -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, KeyChord, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from typing import List  # noqa: F401
from libqtile.backend.x11 import window
from libqtile.confreader import ConfigError
from libqtile.widget import base

### INSTALL DECORATIONS FROM HERE //// INSTALL AS SUDO  https://github.com/elparaguayo/qtile-extras.git
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration

XEMBED_PROTOCOL_VERSION = 0



#=-/ Created variables /-=#
mod = "mod4"
mod1 = "alt"
mod2 = "control"
myTerm = "kitty"
myVol = "pulse"
# myBrowser = "google-chrome-stable"
# logoutMenu = "kitty -e herbst-logout.sh"

#=-/ Keybindings /-=#
keys = [
         #=-/ Main sys control /-=#
        Key([mod], "z", lazy.next_layout(), desc='Toggle through layouts'),
        Key([mod], "q", lazy.window.kill(), desc='Kill active window'),
        Key([mod, "shift"], "r", lazy.restart(), desc='Restart Qtile'),
        #=-/ Terminals /-=#
        Key([mod], "Return", lazy.spawn("kitty -e fish"), desc='Run Launcher'),
        Key([mod, "shift"], "Return", lazy.spawn(" terminator -e fish "), desc='kitty'),
        Key([mod], "r", lazy.spawn("feh --randomize --bg-fill /home/dmne/Pictures/background")),
        # Key([mod], "space", lazy.spawn(" cerebro")),
        Key([mod], "space", lazy.spawn("rofi -show drun -show-icons -modi drun,run")),
        Key([mod2,"shift"], "space", lazy.spawn("kitty -e  /home/dmne/.config/nnn/plugins/launch")),
        # Key([mod2], "space", lazy.spawn("rofi -show calc")),
        Key([mod2], "space", lazy.spawn(" galculator")),
        Key([mod, "shift"], "x", lazy.spawn("i3lock-fancy"), desc='betterlockscreen'),
        # Key([mod, "shift"], "x", lazy.spawn("betterlockscreen -l blur"), desc='betterlockscreen'),
        Key([mod], "x", lazy.spawn("kitty  -e herbst-logout.sh")),
        #Key([mod], "x", lazy.spawn(" archlinux-logout ")),
        # Key([mod], "x", lazy.spawn(".config/rofi/powermenu.sh ")),
        Key([mod], "t", lazy.spawn("pcmanfm")),
        Key([mod], "e", lazy.spawn("kitty -e micro /home/dmne/.config/qtile/config.py")),
        Key([mod], "o", lazy.spawn("obsidian")),
        Key([mod], "d", lazy.spawn("org.telegram.desktop ")),
        Key([mod], "m", lazy.spawn("kitty -e mocp")),
        Key([mod, "shift"], "t", lazy.spawn("kitty -e ranger"), desc='NNN'),
        #=-/ Browsers /-=#
        Key([mod], "w", lazy.spawn(" org.mozilla.firefox "), desc='chromium-browser'),
        Key([mod, "shift"], "w", lazy.spawn("com.google.Chrome"), desc='Chrome'),

        #######  VOLUME WITH PAMIXER
        Key([mod2], "bracketright", lazy.spawn("/home/dmne/.local/bin/changevolume up"), desc='volume-up'),
        Key([mod2], "bracketleft", lazy.spawn("/home/dmne/.local/bin/changevolume down"), desc='volume-down'),
        Key([mod2], "backslash", lazy.spawn("/home/dmne/.local/bin/changevolume mute"), desc='mute'),
        # Key([mod2], "bracketright", lazy.spawn("pamixer --increase 5"), desc='volume-up'),
        # Key([mod2], "bracketleft", lazy.spawn("pamixer --decrease 5"), desc='volume-down'),
        # Key([mod2], "equal", lazy.spawn("pamixer --toggle-mute"), desc='mute'),

        # Emacs programs launched using the key chord CTRL+e followed by 'key'
        KeyChord([mod],"i", [
            Key([], "e",
                lazy.spawn("code"),
                desc='vscode'
                ),
            Key([], "return",
                lazy.spawn("kitty -e fish"),
                desc='Terminal'
                ),
            Key([], "w",
                lazy.spawn("brave-browser"),
                desc='Brave'
                ),
            Key([], "y",
                lazy.spawn(" opera"),
                desc='Opera'
                ),
            Key([], "a",
                lazy.spawn("kitty -e mocp"),
                desc='MOCP Music Player')
        ]),


         #=-/ Window manipulation /-=#
        #  Key([mod], "j", lazy.layout.down(), desc='Move focus down in current stack pane'),
        #  Key([mod], "k", lazy.layout.up(), desc='Move focus up in current stack pane'),
         Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
         Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
         Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
         Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

         Key([mod], "h", lazy.layout.shrink(), lazy.layout.decrease_nmaster(), desc='Shrink window (MonadTall), decrease number in master pane (Tile)'),
         Key([mod], "l", lazy.layout.grow(), lazy.layout.increase_nmaster(), desc='Expand window (MonadTall), increase number in master pane (Tile)'),
         # Key([mod,"shift"], "n", lazy.layout.normalize(), desc='normalize window size ratios'),
         # Key([mod,"shift"], "m", lazy.layout.maximize(), desc='toggle window between minimum and maximum sizes'),
         Key([mod], "f", lazy.window.toggle_fullscreen(), desc='toggle fullscreen'),
         Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc='toggle float'),

         #=-/ Stack and master manipulation /-=#
         Key([mod, "shift"], "z", lazy.layout.rotate(), lazy.layout.flip(), desc='flip master and stack'),
         Key([mod], "Tab", lazy.layout.next(), desc='Switch window focus to other pane(s) of stack'),

         #=-/ Multimedia keys /-=#
         # Key([], "XF86AudioLowerVolume", lazy.spawn("pactl set-sink-volume 0 -5%")),
         # Key([], "XF86AudioRaiseVolume", lazy.spawn("pactl set-sink-volume 0 +5%")),
         # Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),

        ##### WIREPLUMBER VOLUME CONTROLS
         Key([], "XF86AudioLowerVolume", lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-")),
         Key([], "XF86AudioRaiseVolume", lazy.spawn("wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%+")),
         Key([], "XF86AudioMute", lazy.spawn("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle")),
        

        # INCREASE/DECREASE BRIGHTNESS
        Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 10")),
        Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 10")),

        # INCREASE/DECREASE/MUTE VOLUME
        # Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
        # Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
        # Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),

        Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
        Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
        Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
        Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

         #=-/ Scratchpads /-=#
         Key([mod2], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
         Key([mod2], "2", lazy.group['manager'].dropdown_toggle('nnn')),
         Key([mod2], "3", lazy.group['pulse'].dropdown_toggle('mixer')),
         Key([mod2], "4", lazy.group['tel'].dropdown_toggle('telegram')),
         Key([mod2], "9", lazy.group['music'].dropdown_toggle('tunes')),
         Key([mod2], "0", lazy.group['logout'].dropdown_toggle('exitMenu')),
]

#=-/ Window groups settings /-=#
groups = [Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          Group("", layout='monadtall'),
          #=-/ Scratchpad groups /-=#
          ScratchPad("music",[DropDown("tunes", "kitty -e mocp", x=0.2, y=0.02, width=0.60, height=0.43, on_focus_lost_hide=False)]),
          # ScratchPad("pulse",[DropDown("mixer", "kitty -e pulsemixer", x=0.33, y=0.02, width=0.35, height=0.95, on_focus_lost_hide=False)]),
          ScratchPad("logout",[DropDown("exitMenu", "/usr/bin/clearine ", x=0.40, y=0.30, width=0.20, height=0.20, on_focus_lost_hide=False)]),
          ScratchPad("tel",[DropDown("telegram", "telegram-desktop", x=0.12, y=0.02, width=0.75, height=0.6, on_focus_lost_hide=False)]),
          ScratchPad("scratchpad",[DropDown("term", "kitty -e fish", x=0.12, y=0.02, width=0.75, height=0.3, on_focus_lost_hide=False)]),
          ScratchPad("manager",[DropDown("nnn", "kitty -e nnn", x=0.35, y=0.02, width=0.3, height=0.80, on_focus_lost_hide=False)]),
          ScratchPad("pulse",[DropDown("mixer", "kitty -e pulsemixer", x=0.12, y=0.02, width=0.75, height=0.3, on_focus_lost_hide=False)]),
]

from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder("mod4")

#=-/ Layout settings /-=#
layout_theme = {"border_width": 3,
                "margin": 13,
                "border_focus": "#006AFF",
                "border_normal": "#FF8000"
                }

layouts = [
    layout.MonadThreeCol(**layout_theme)
    # layout.MonadTall(**layout_theme),
    # layout.MonadWide(**layout_theme),
    #layout.Columns(**layout_theme),
    #layout.Matrix(**layout_theme),
    # layout.Zoomy(**layout_theme),
    #layout.Stack(num_stacks=2),
    #layout.Tile(shift_windows=True, **layout_theme),
    # layout.Bsp(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Max(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Floating(**layout_theme)
    # layout.TreeTab(
    #      font = "Ubuntu",
    #      fontsize = 10,
    #      sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
    #      section_fontsize = 10,
    #      border_width = 2,
    #      bg_color = "1c1f24",
    #      active_bg = "c678dd",
    #      active_fg = "000000",
    #      inactive_bg = "a9a1e1",
    #      inactive_fg = "1c1f24",
    #      padding_left = 0,
    #      padding_x = 0,
    #      padding_y = 5,
    #      section_top = 10,
    #      section_bottom = 20,
    #      level_shift = 8,
    #      vspace = 3,
    #      panel_width = 200
    #      )
]

#=-/ System colors /-=#
colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#2880FF", "#2880FF"],
          ["#a9a1e1", "#a9a1e1"]]

#=-/ Default settings for widgets /-=#
widget_defaults = dict(
    font="Ubuntu Nerd Font Bold",  ### NERD FONT https://www.nerdfonts.com/font-downloads
    fontsize = 10,
    padding = 2,
    # background="#00000088"
    background="#000000"
)
extension_defaults = widget_defaults.copy()

#=-/ Widgets /-=#
def init_widgets_list():
    widgets_list = [
                    # widget.CurrentLayout(),
                    widget.GroupBox(
                         # disable_drag=True,
                         font ='Ubuntu Nerd Font Bold',
                         fontsize = 20,
                         # active="#FF006D",
                         active="#2880ff",
                         inactive="#c1c1c1",
                         this_current_screen_border = "#05ff00",
                         rounded=True,
                         highlight_method='text',
                         highlight_text_color='red',
                         borderwidth=4,
                         # highlight_color="#5f79FF",
                        #  this_current_screen_boarder="#ffffff",
                        #  this_screen_boarder="#000000",
                        #  other_current_screen_boarder="#3b6699",
                         # highlight_color= ['#ffffff', '#00ffff'],
                         # background="#00000088",
                         background="#000000",
                         fourground = "#c1c1c1",
                        #  foreground="#FF8000",
                        #  background_inactive='#ffffff',
                         # background_active='#ffffff',
                         padding = 1,
                         decorations=[
                           BorderDecoration(
                               colour = "#c1c1c1",
                               border_width = [0, 0, 3, 0],
                               padding_x = 0,
                               padding_y = None
                           )
                    ],
                    ),


                      widget.Sep(
                        background="#000000",
                        foreground="#000000",
               #        linewidth="0",
                        padding=10,
                        decorations=[
                           BorderDecoration(
                            #    colour = colors[9],
                               colour = "#000000",
                                # colour = "#2880FF",
                               border_width = [0, 0, 3, 0],
                               padding_x = 0,
                               padding_y = None,
                           )
                    ],
                    ),

                    widget.WindowName(
                       foreground="#05ff00",
                       background="#000000",
                       # background="#000000",
                       font="Ubuntu Nerd Font Bold ",
                       fontsize=8,
                       padding = 0,
                         decorations=[
                           BorderDecoration(
                            #    colour = colors[9],
                               colour = "#05ff00",
                               border_width = [0, 0, 3, 0],
                               padding_x = 0,
                               padding_y = None
                           )
                    ],
                    ),


                      widget.Sep(
                        background="#000000",
                        foreground="#000000",
               #        linewidth="0",
                        padding=8,
                        decorations=[
                           BorderDecoration(
                            #    colour = colors[9],
                               colour = "#000000",
                                # colour = "#2880FF",
                               border_width = [0, 0, 3, 0],
                               padding_x = 0,
                               padding_y = None,
                           )
                    ],
                    ),

                    #   widget.Visualiser(
                    #    autostart=True,
                    #    bar_colour="#FFE065",
                    #    background="#000000",
                    #    bar_height=20,
                    #    bars=20,
                    #    hide=False,
                    #    framerate=25,
                    #    spacing=2,
                    #    width=120,
                    # #    font="Ubuntu Nerd Font Bold ",
                    # #    fontsize=8,
                    #    padding = 0,
                    #      decorations=[
                    #        BorderDecoration(
                    #         #    colour = colors[9],
                    #            colour = "#FFE065",
                    #            border_width = [0, 0, 3, 0],
                    #            padding_x = 0,
                    #            padding_y = None
                    #        )
                    # ],
                    # ),

                    # widget.Chord(
                    #   chords_colors={
                    #     "launch": ("#ff0000", "#ffffff"),
                    # },
                    #    name_transform=lambda name: name.upper()
                    # ),


            #       widget.GenPollText(
            #            name = "ytsubs",
            #            fmt = " " " {} ", update_interval = 3600,
            #            foreground = colors[1], background = colors[7],
            #            func = lambda: subprocess.check_output("/home/jake/.local/scripts/ytsubs.sh").decode("utf-8"),
            #            padding = 0
            #       ),
                    widget.Moc(
                         background="#000000",
                         foreground="#FF006D",
                         font="Ubuntu Nerd Font Bold ",
                         fontsize=9,
                         update_interval=1,
                         padding = 0,
                         decorations=[
                           BorderDecoration(
                            #    colour = colors[9],
                               colour = "#FF006D",
                               border_width = [0, 0, 3, 0],
                               padding_x = 0,
                               padding_y = None
                    #    widget.Cmus(
                    #      background="#000000",
                    #      foreground="#FF29C2",
                    #      font="Ubuntu Bold Italic ",
                    #      fontsize= 7,
                    #      update_interval=0.5,
                    #      markup="true",
                    #      max_chars=35,
                    #      noplay_color="#ff0000",
                    #      play_color="#FF29C2",
                    #      scroll="true",
                    #      padding = 2,
                    #      decorations=[
                    #        BorderDecoration(
                    #         #    colour = colors[9],
                    #            colour = "#FF29C2",
                    #            border_width = [0, 0, 3, 0],
                    #            padding_x = 0,
                    #            padding_y = None
                           )
                    ],
                    ),

                      widget.Sep(
                        background="#000000",
                        foreground="#000000",
               #        linewidth="0",
                        padding=8,
                        decorations=[
                           BorderDecoration(
                            #    colour = colors[9],
                               colour = "#000000",
                                # colour = "#2880FF",
                               border_width = [0, 0, 3, 0],
                               padding_x = 0,
                               padding_y = None,
                           )
                    ],
                    ),


                    widget.CryptoTicker(
                         crypto="BTC",
                         # foreground="#2880FF",
                         foreground="#FEDE00",
                         background="#000000",
                         # background="#000000",
                         currency = "USD",
                         symbol = "$",
                         font = "Ubuntu Nerd Font Bold",
                         fontsize ="9",
                         padding = 2,
                         decorations=[
                           BorderDecoration(
                            #    colour = colors[9],
                               colour = "#FEDE00",
                               border_width = [0, 0, 3, 0],
                               padding_x = 0,
                               padding_y = None
                           )
                    ],
                    ),
                    widget.Sep(
                        background="#000000",
                        foreground="#000000",
               #        linewidth="0",
                        padding=1,
                        decorations=[
                           BorderDecoration(
                            #    colour = colors[9],
                               colour = "#000000",
                               border_width = [0, 0, 3, 0],
                               padding_x = 0,
                               padding_y = None,
                           )
                    ],
                    ),




                    widget.Sep(
                        background="#000000",
                        foreground="#000000",
               #        linewidth="0",
                        padding=8,
                        decorations=[
                           BorderDecoration(
                            #    colour = colors[9],
                               colour = "#ff0011",
                               border_width = [0, 0, 0, 0],
                               padding_x = 0,
                               padding_y = None,
                           )
                    ],
                    ),


                    widget.Net(
                        font="FiraCode Bold",
                        fontsize=12,
                        interface="enp4s0",
#                        interface="wlan0",
                        # format = '{down} ↓↑ {up}',
                        # format='{down:.0f}{down_suffix} ↓↑ {up:.0f}{up_suffix}',
                        format = '{down:6.0f}{down_suffix:<2}↓↑{up:1.0f}{up_suffix:<2}',
                        # prefix='M',
                        foreground="#b63cff",
                        background="#000000",
                        padding = 0,
                        decorations=[
                           BorderDecoration(
                            #    colour = colors[9],
                               colour = "#b63cff",
                               border_width = [0, 0, 3, 0],
                               padding_x = 0,
                               padding_y = None,
                           )
                    ],
                    ),

                    widget.Sep(
                        background="#000000",
                        foreground="#000000",
               #        linewidth="0",
                        padding=1,
                        decorations=[
                           BorderDecoration(
                            #    colour = colors[9],
                               colour = "#ff0011",
                               border_width = [0, 0, 0, 0],
                               padding_x = 0,
                               padding_y = None,
                           )
                    ],
                    ),
                    widget.Sep(
                        background="#000000",
                        foreground="#000000",
               #        linewidth="0",
                        padding=8,
                        decorations=[
                           BorderDecoration(
                            #    colour = colors[9],
                               colour = "#da8548",
                               border_width = [0, 0, 0, 0],
                               padding_x = 0,
                               padding_y = None,
                           )
                    ],
                    ),

                    widget.CPU(
                       #format="CPU {freq_current}GHz {load_percent}%",
                       font="FiraCode Bold",
                       fontsize=12,
                       foreground="#FF8000",
                       background="#000000",
                       # background="#000000",
                       threshold = 90,
                       padding = 0,
                       decorations=[
                           BorderDecoration(
                            #    colour = colors[9],
                               colour = "#ff8000",
                               border_width = [0, 0, 3, 0],
                               padding_x = 0,
                               padding_y = None,
                           )
                    ],
                    ),
                    widget.Sep(
                        background="#000000",
                        foreground="#000000",
               #        linewidth="0",
                        padding=8,
                        decorations=[
                           BorderDecoration(
                            #    colour = colors[9],
                               colour = "#ff8000",
                               border_width = [0, 0, 0, 0],
                               padding_x = 0,
                               padding_y = None,
                           )
                    ],
                    ),



                    # widget.Memory(
                    #     background="#000000",
                    #     foreground="#FF8000",
                    #     padding=10
                    #  #  font=
                    # # fontsize=9,
                    # ),

                    widget.Memory(
                        font="FiraCode Bold",
                        fontsize=12,
                        foreground = "#2880FF",
                        background = "#000000",
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
                        fmt = 'Mem:{}',
                        padding = 0,
                        decorations=[
                           BorderDecoration(
                               colour = "#2880FF",
                               border_width = [0, 0, 3, 0],
                               padding_x = 0,
                               padding_y = None,
                           )
                    ],
                    ),
                    widget.Sep(
                        background="#000000",
                        foreground="#000000",
                    #   linewidth="0",
                        padding=8
                    ),

                    # widget.DF(
                        # foreground="#ffffff",
                        # background="#000000",
                        # fmt = '/:{}',
                        # partition = "/",
                    #     padding=0,
                    #     decorations=[
                    #        BorderDecoration(
                    #            colour = "#05ff00",
                    #            border_width = [0, 0, 3, 0],
                    #            padding_x = 0,
                    #            padding_y = None
                    #         )
                    #    ],
                    # ),



                    # widget.ThermalSensor(
                    #     foreground = "#f3f50c",
                    #     foreground_alert = "#FF0000",
                    #     background = "#000000",
                    #     metric = True,
                    #     padding = 3,
                    #     threshold = 80
                    # ),

                    widget.ThermalSensor(
                        font="FiraCode Bold",
                        fontsize=12,
                        foreground = "#05ff00",
                        foreground_alert = "ff0000",
                        background = "#000000",
                        tag_sensor = "Tctl",
                        update_interval = 2,
                        threshold = 70,
                        fmt = 'Temp: {}',
                        padding = 0,
                        decorations=[
                           BorderDecoration(
                               colour = "#05ff00",
                               border_width = [0, 0, 3, 0],
                               padding_x = 0,
                               padding_y = None
                            )
                       ],
                    ),
                    widget.Sep(
                        background="#000000",
                        foreground="#000000",
                    #   linewidth="0",
                        padding=8
                    ),

                    # widget.Clock(
                    #    foreground = "#c1c1c1",
                    #    background = "#000000",
                    #    format = "%a %b %d  %H:%M",
                    #    padding = 5
                    # ),
                    widget.Clock(
                        font="FiraCode Bold",
                        fontsize=12,
                        foreground = "#c1c1c1",
                        background = "#000000",
                        format = "%a %b %d %H:%M:%S",
                        decorations=[
                           BorderDecoration(
                               colour = "#c1c1c1",
                               border_width = [0, 0, 3, 0],
                               padding_x = 0,
                               padding_y = None,
                           )
                    ],

                    ),
                    widget.Sep(
                        background="#000000",
                        foreground="#000000",
                    #   linewidth="0",
                        padding=8
                    ),

                    widget.Volume(
                        font="Ubuntu Nerd Font Bold",
                        fontsize=12,
                        # fmt = "",
                        fmt = 'Vol {}',
                        # step = 5,
                        foreground = "#00FFFF",
                        background = "#000000",
                        mouse_callbacks = {'Button3':lazy.group['pulse'].dropdown_toggle('mixer')},
                        # format = "%a %b %d %H:%M:%S",
                        decorations=[
                           BorderDecoration(
                               colour = "#00FFFF",
                               border_width = [0, 0, 3, 0],
                               padding_x = 0,
                               padding_y = None,
                           )
                    ],

                    ),
                    widget.Sep(
                        background="#000000",
                        foreground="#000000",
                    #   linewidth="0",
                        padding=5
                    ),

                    widget.Systray(
                        #background="#878787",
                        # background="#737C85",
                        background="#000000",
                        padding=0,
                        decorations=[
                           BorderDecoration(
                               colour = "#ffffff",
                               border_width = [0, 0, 0, 0],
                               padding_x = 0,
                               padding_y = None
                           )
                    ],

                    ),


              ]

    return widgets_list

#=-/ Set bar to screen /-=#
def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

#=-/ Set bar height and opacity, also set wallpaper /-=#
def init_screens():
    return [Screen(top=bar.Bar(
        widgets=init_widgets_screen1(),
        # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
        # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        # margin=[0, 26, 5, 10], ### FOR BROKEN LAPTOP
        margin=[8, 0, 0, 0],
        background='#000000',
        # background='#000000',
        opacity=1.0,
        size=24))]
        # wallpaper='~/.config/herbstluftwm/wallpaper/teal/city.jpg',
        # wallpaper_mode='fill')]

#=-/ Initiate functions for screens and widgets /-=#
if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()

#=-/ Mouse settings /-=#
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

#=-/ Cursor rules /-=#
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = True

#=-/ Window rules /-=#

floating_layout = layout.Floating(
    border_width=3,
    border_focus="#2880FF",
    border_normal="#FF8000",
    float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(wm_type="utility"),
    Match(wm_type="notification"),
    Match(wm_type="toolbar"),
    Match(wm_type="pop-up"),
    Match(wm_type="splash"),
    Match(wm_type="dialog"),
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'), # GPG key password entry
    Match(wm_class="confirmreset"),  # gitk
    Match(wm_class="makebranch"),  # gitk
    Match(wm_class="maketag"),  # gitk
    Match(wm_class="Galculator"),  # gitk Galculator
    Match(wm_class="galculator"),  # gitk Galculator
    Match(wm_class="blueman-manager"),  # gitk
    Match(wm_class="blueberry.py"),  # gitk
    Match(wm_class="ssh-askpass"),  # ssh-askpass
    Match(wm_class="Gpick"),  # ssh-askpass
    Match(wm_class="gpick"),  # ssh-askpass
    Match(wm_class="gammy"),  # ssh-askpass
    Match(wm_class="Gammy"),  # ssh-askpass
    Match(wm_class="browser-window"),  # ssh-askpass
    Match(wm_class="Skype"),  # ssh-askpass
    Match(wm_class="Yad"),  # ssh-askpass
    Match(wm_class="cachybrowser"),  # ssh-askpass
    Match(wm_class="Steam"),  # ssh-askpass
    Match(wm_class="steamwebhelper"),  # ssh-askpass
    Match(wm_class="telegram-desktop"),  # ssh-askpass
    Match(wm_class="Variety"),  # ssh-askpass
    Match(wm_class="xpad"),  # ssh-askpass
    Match(wm_class="NoiseTorch"),  # ssh-askpass
    Match(wm_class="localsend_app"),  # ssh-askpass
    # Match(wm_class="google-chrome"),  # ssh-askpass
    Match(wm_class="pavucontrol"),  # ssh-askpass
    Match(wm_class="Imager"),  # ssh-askpass
    Match(wm_class="timeshift"),  # ssh-askpass         
    Match(wm_class="livecaptions"),  # ssh-askpass
    Match(wm_class="crx_fcfcfllfndlomdhbehjjcoimbgofdncg"),  # ssh-askpass
    Match(wm_class="system-config-printer"),  # ssh-askpass
    Match(wm_class="crx_dmkamcknogkgcdfhhbddcghachkejeap"),  # ssh-askpass
    Match(wm_class="crx_nkbihfbeogaeaoehlefnkodbefgpgknn"),  # ssh-askpass
    Match(wm_class="crx_jiidiaalihmmhddjgbnbgdfflelocpak"),  # ssh-askpass
    Match(wm_class="crx_mfgccjchihfkkindfppnaooecgfneiii"),
    Match(wm_class="Scanner"),  # ssh-askpass
    Match(wm_class="InfinityWallet"),  # ssh-askpass
    Match(title="branchdialog"),  # gitk
    Match(title="pinentry"),  # GPG key password entry

])


# auto_fullscreen = True
focus_on_window_activation = "smart"

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
