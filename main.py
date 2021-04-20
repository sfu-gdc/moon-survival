import signal
import sys
from functools import partial

import curses
from curses import wrapper

from model.world import World
from mytypes import Direction
from scenes import init_scenes, exit_scenes, loop_current_scene, change_scene_to
import view

# ----------- Globals  ----------- #

world = None
should_exit = False
commands = None

# ----------- Commands ----------- #

def cmd_help():
    view.putcln("{bm}List of commands: {}")
    view.put("\t")
    view.putlist(commands.keys(), delim=" | ", newline=True)

def cmd_exit():
    global should_exit
    should_exit = True
    view.putln("Bye!")

def cmd_yell():
    view.putcln("{y}Nobody hears you, as the moon has very little atmosphere.{}")

# ----------- Main game loop ----------- #

def start(window):
    global world, commands, scenes, current_scene

    # window & corner-case setup 
    signal.signal(signal.SIGINT, lambda sig, frame: end(window))

    # game setup
    world = World()
    commands = {
        "help": cmd_help, 
        "exit": cmd_exit, 
        "view": world.display_map, 
        "scan": world.display_scanned_map, 
        "stats": world.player.display_stats, 
        "control mode": lambda: change_scene_to("control_mode"),
        "move north": partial(world.move_player, Direction.North), 
        "move east": partial(world.move_player, Direction.East), 
        "move south": partial(world.move_player, Direction.South), 
        "move west": partial(world.move_player, Direction.West), 
        "yell": cmd_yell }
    
    init_scenes("terminal_mode", window, world) # TODO: should start with "active_mode" or "menu"

def game_loop():
    loop_current_scene()

def end(window):
    exit_scenes()

    # revert curses settings
    curses.nocbreak()
    window.keypad(False)
    curses.echo()

    # exit the window
    curses.endwin()

    view.putln("exiting nicely...")
    sys.exit(0)

if __name__ == "__main__":
    def main(window):
        start(window)
        
        while not should_exit:
            game_loop()

        end(window)

    wrapper(main) # helpful for debugging purposes.