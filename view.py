import sys, re, os

_state = {} # TODO: test to double check this state is synchonized.

def put(txt, end="", flush=False):
    print(txt, end=end, flush=flush)

def putln(txt, flush=False):
    put(txt, end="\n", flush=flush)

# see: https://en.wikipedia.org/wiki/ANSI_escape_code#Colors
# ex: bw -> bright white; k is black; _ means background
_COLOUR_CODES = {
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
}

_VALID_COLOURS = "|".join(_COLOUR_CODES.keys())
_colour_pattern = r'\{(' + _VALID_COLOURS + r')\}'
_colour_pattern = re.compile(_colour_pattern)

# put colours like {r}redstuff!{r} -> use \{ to escape.
def putc(txt, end="", flush=False):
    sub_colour_code = lambda matchobj: _COLOUR_CODES[matchobj.group(0).strip("{}")]
    txt = re.sub(_colour_pattern, sub_colour_code, txt)
    put(txt.replace("\\{", "{").replace("\\}", "}"), end, flush)

if os.name == "nt":
    os.system("color")

def putcln(txt, flush=False):
    putc(txt, end="\n", flush=flush)

def putlist(list, delim=", ", newline=False):
    list = iter(list)
    
    put(next(list))
    for item in list:
        put(delim + str(item))

    if newline:
        sys.modules[__name__].newline()

def newline():
    print("\n", end="")
