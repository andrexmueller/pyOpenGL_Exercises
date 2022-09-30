import os
from enum import Enum


"""
ANSI Escape
"""

class TextAttr:
    CLEAN_ATTR = 0
    BOLD = 1
    UNDERSCORE = 4
    BLINK = 5  
    REVERSE_COLOR = 7
    CONCEALED = 8


class FGColor:
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 34
    CYAN = 36
    WHITE = 37


class BGColor:
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    MAGENTA = 45
    CYAN = 46
    WHITE = 47


def cprint(text: str, fg=FGColor.WHITE, bg=BGColor.BLACK, attr=None) -> None:
    os.system('')
    if attr:
        print(f"\x1b[{fg};{bg};{attr}m{text} \x1b[0m")    
    else:
        print(f"\x1b[{fg};{bg}m{text} \x1b[0m")
    return



# os.system('') #enable VT100 Escape Sequence for WINDOWS 10 Ver. 1607

# print('\x1b[34;47m' + "teste teste teste" + '\x1b[0m')
# print('\x1b[4;34;47m' + "teste teste teste" + '\x1b[0m')
# print('\x1b[1;34;47m' + "teste teste teste" + '\x1b[0m')
# print('\x1b[7;34;47m' + "teste teste teste" + '\x1b[0m')
# print('\x1b[47;34m' + "teste teste teste" + '\x1b[0m')
# print('\x1b[8;36m' + "teste .........teste teste" + '\x1b[0m')


cprint("Testando 1 2 3 , 1 2 3", FGColor.CYAN, BGColor.YELLOW)
cprint("Testando 1 2 3 , 1 2 3", FGColor.CYAN, BGColor.BLUE, TextAttr.UNDERSCORE)
cprint("Testando 1 2 3 , 1 2 3", FGColor.CYAN, BGColor.YELLOW, TextAttr.BLINK)
