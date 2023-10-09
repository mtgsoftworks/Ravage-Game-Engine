from ravage2d import __USE_ANSI_COLORS
from ravage2d.libs.terminal import RESET, FG


def warn(message):
    if __USE_ANSI_COLORS: print(f"{FG.orange}WARNING:{RESET} {message}")
    else: print(f"WARNING: {message}")



class NoStageDeclared(Exception): pass
class UnknownKey(Exception): pass
class UnknownMouseButton(Exception): pass
class UnknownControllerButton(Exception): pass
class DeviceNotFound(Exception): pass
class NetworkingError(Exception): pass
class AnimationNotMatched(Exception): pass
