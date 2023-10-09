import os

from ravage2d.libs import utils

# disable Pygame welcome message
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"
import pygame

from ravage2d.libs import specs
specs.OS.update_info()
specs.Monitor.update_info()

class DISPATCHER: pass

if "ravage2d_DISABLE_ANSI_COLORS" in os.environ: __USE_ANSI_COLORS = False
else: __USE_ANSI_COLORS = True

from ravage2d.libs.terminal import REVERSE, RESET, FG, clear

clear()

from ravage2d.version import *

from ravage2d.engine import     Engine
from ravage2d.stage import      Stage
from ravage2d.gameobject import GameObject
from ravage2d.sprite import     Sprite
from ravage2d.timer import      Timer
from ravage2d.audio import      Sound
from ravage2d.color import      Color, Palette
from ravage2d.trigger import    Trigger

if "ravage2d_HIDE_WELCOME_MESSAGE" not in os.environ:
    if __USE_ANSI_COLORS:
        print(f"\u2588" + "\u2580"*20 + f"\u2588")
        print(f"\u2588{FG.lightred}       Ravage2D       {RESET}\u2588 Version : {ravage2d_VERSION}")
        print(f"\u2588{FG.orange}    GAME ENGINE     {RESET}\u2588 State   : {ravage2d_VERSION_STATE.capitalize()}")
        print("\u2588" + "\u2584"*20 + "\u2588\n")
    else:
        print(f"\u2588" + "\u2580"*20 + f"\u2588")
        print(f"\u2588       ravage2d       \u2588 Version : {ravage2d_VERSION}")
        print(f"\u2588    GAME ENGINE     \u2588 State   : {ravage2d_VERSION_STATE.capitalize()}")
        print("\u2588" + "\u2584"*20 + "\u2588\n")

del os, pygame, libs, engine, errors, window, gameobject, renderer, audio, \
    sprite, stage, timer, trigger, REVERSE, RESET, FG
