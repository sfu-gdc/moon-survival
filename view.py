import sys, re, os
import curses

from mytypes import Vector2D

# ----------- Global Variables ----------- #

# see: https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
# ex: bw -> bright white; k is black; _ means background
OLD_COLOUR_CODES = {
    "k" : "\033[30m",
    "r" : "\033[31m",
    "g" : "\033[32m",
    "y" : "\033[33m",
    "b" : "\033[34m",
    "m" : "\033[35m",
    "c" : "\033[36m",
    "w" : "\033[37m",
    "_k" : "\033[40m",
    "_r" : "\033[41m",
    "_g" : "\033[42m",
    "_y" : "\033[43m",
    "_b" : "\033[44m",
    "_m" : "\033[45m",
    "_c" : "\033[46m",
    "_w" : "\033[47m",
    
    "bk" : "\033[90m",
    "br" : "\033[91m",
    "bg" : "\033[92m",
    "by" : "\033[93m",
    "bb" : "\033[94m",
    "bm" : "\033[95m",
    "bc" : "\033[96m",
    "bw" : "\033[97m",
    "_bk" : "\033[100m",
    "_br" : "\033[101m",
    "_bg" : "\033[102m",
    "_by" : "\033[103m",
    "_bb" : "\033[104m",
    "_bm" : "\033[105m",
    "_bc" : "\033[106m",
    "_bw" : "\033[107m",

    "bold" : "\033[1m",
    "rev" : "\033[7m",
    "" : "\033[0m", # end colour -> } is returned cause it can't point to ""

    "none" : "" # helps with logic
}
EndColour = OLD_COLOUR_CODES[""]

brighten_color = curses.A_BOLD | curses.A_REVERSE
CURSES_COLOUR_CODES = {
    "k" : curses.COLOR_BLACK,
    "r" : curses.COLOR_RED,
    "g" : curses.COLOR_GREEN,
    "y" : curses.COLOR_YELLOW,
    "b" : curses.COLOR_BLUE,
    "m" : curses.COLOR_MAGENTA,
    "c" : curses.COLOR_CYAN,
    "w" : curses.COLOR_WHITE,

    "_k" : curses.COLOR_BLACK,
    "_r" : curses.COLOR_RED,
    "_g" : curses.COLOR_GREEN,
    "_y" : curses.COLOR_YELLOW,
    "_b" : curses.COLOR_BLUE,
    "_m" : curses.COLOR_MAGENTA,
    "_c" : curses.COLOR_CYAN,
    "_w" : curses.COLOR_WHITE,
    
    "bk" : curses.COLOR_BLACK,
    "br" : curses.COLOR_RED,
    "bg" : curses.COLOR_GREEN,
    "by" : curses.COLOR_YELLOW,
    "bb" : curses.COLOR_BLUE,
    "bm" : curses.COLOR_MAGENTA,
    "bc" : curses.COLOR_CYAN,
    "bw" : curses.COLOR_WHITE,

    "_bk" : curses.COLOR_BLACK,
    "_br" : curses.COLOR_RED,
    "_bg" : curses.COLOR_GREEN,
    "_by" : curses.COLOR_YELLOW,
    "_bb" : curses.COLOR_BLUE,
    "_bm" : curses.COLOR_MAGENTA,
    "_bc" : curses.COLOR_CYAN,
    "_bw" : curses.COLOR_WHITE,
    
    "bold" : curses.A_BOLD,
    "rev" : curses.A_REVERSE,
    "" : None,

    #"none" : "" # helps with logic?
}

# TODO: check if bright background colors exist.
VALID_COLOUR_TOKENS = {
    "k", "r", "g", "y", "b", "m", "c", "w",
    "_k", "_r", "_g", "_y", "_b", "_m", "_c", "_w",
    
    "bk", "br", "bg", "by", "bb", "bm", "bc", "bw",
    "_bk", "_br", "_bg", "_by", "_bb", "_bm", "_bc", "_bw",

    "bold",
    "rev",
    "",
}

BRIGHT_COLOUR_TOKENS = {
    "bk", "br", "bg", "by", "bb", "bm", "bc", "bw",
    "_bk", "_br", "_bg", "_by", "_bb", "_bm", "_bc", "_bw",
}

BACKGROUND_COLOUR_TOKENS = {
    "_k", "_r", "_g", "_y", "_b", "_m", "_c", "_w",
    "_bk", "_br", "_bg", "_by", "_bb", "_bm", "_bc", "_bw",
}

Size = Vector2D(20, 10)

# ----------- Local Variables ----------- #

_VALID_COLOURS = "|".join(CURSES_COLOUR_CODES.keys())
_colour_pattern = r'(\{(?:' + _VALID_COLOURS + r')\})'
_colour_pattern = re.compile(_colour_pattern)

# ----------- Colour functions ----------- #

# parses a color tokens in a string and puts it all on the same line
def putcolor(window, txt):
    token_list = re.split(_colour_pattern, txt)
    state = []
    for token in token_list[1:-1]:
        if (len(state) == 0 or len(state) == 2) and token[1:-1] in VALID_COLOUR_TOKENS:
            state.append(token[1:-1])
            if len(state) == 3: # NOTE: this may not be the most efficient, but it works.
                if state[0] in BRIGHT_COLOUR_TOKENS:
                    curses.init_pair(1, CURSES_COLOUR_CODES[state[0]], curses.COLOR_BLACK)
                    window.addstr(state[1], curses.color_pair(1)) #| brighten_color
                elif state[0] in BACKGROUND_COLOUR_TOKENS:
                    curses.init_pair(1, curses.COLOR_WHITE, CURSES_COLOUR_CODES[state[0]])
                    window.addstr(state[1], curses.color_pair(1)) #| brighten_color
                else:
                    curses.init_pair(1, CURSES_COLOUR_CODES[state[0]], curses.COLOR_BLACK)
                    window.addstr(state[1], curses.color_pair(1))
                state = []
        elif len(state) == 1:
            state.append(token) # string content
        else:
            # TODO: log these errors to a debug file
            return
    return

# ----------- Put functions ----------- #

# TODO: making all these functions was kinda a poor idea since it's just different names
# for print. TODO: stop using these after I start using *curses*

'''
def put(txt, end="", flush=False):
    print(txt, end=end, flush=flush)

def putln(txt, flush=False):
    put(txt, end="\n", flush=flush)

def newline():
    print("\n", end="")
'''

# put colours like {r}redstuff!{r} -> use \{ to escape.
def putc(txt, end="", flush=False):
    sub_colour_code = lambda matchobj: COLOUR_CODES[matchobj.group(0).strip("{}")]
    txt = re.sub(_colour_pattern, sub_colour_code, txt)
    put(txt.replace("\\{", "{").replace("\\}", "}"), end, flush)

# TODO: keep this function?
def putcln(txt, flush=False):
    putc(txt, end="\n", flush=flush)

def putlist(list, delim=", ", newline=False, col=False):
    myput = putc if col else put

    list = iter(list)
    myput(next(list))

    for item in list:
        myput(delim + str(item))

    if newline:
        sys.modules[__name__].newline()

# -------------------------------------------- #
# Curses Init:
