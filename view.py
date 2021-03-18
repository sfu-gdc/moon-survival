import sys, os, re

_state = {} # TODO: test to double check this state is synchonized.

def put(txt, end="", flush=False):
    print(txt, end=end, flush=flush)

def putln(txt, flush=False):
    print(txt, flush=flush)

'''
# TODO: test if this works properly.
if os.kind == "windows":
    putc = putc_windows
else: # try linux colours otherwise
    putc = put # TODO: implement linux putc

# put colours like {r}redstuff!{r} -> use \{ to escape.
def _putc_windows(txt, end="", flush=False):
    txt.split('{%}') # todo: use regex to insert colour codes... however they work.
    for item in 
'''
def putlist(list, delim=", ", newline=False):
    list = iter(list)
    
    put(next(list))
    for item in list:
        put(delim + str(item))

    if newline:
        sys.modules[__name__].newline()

def newline():
    print("\n", end="")
