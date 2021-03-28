from functools import partial

from model.world import World
from mytypes import Direction
import view

# ----------- Globals  ----------- #

world = None
should_exit = False
commands = None

current_scene = None
scenes = None

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

# ----------- Scenes ----------- #

def command_scene():
    view.put("> ", flush=True)
    cmd = input()

    if cmd in commands:
        commands[cmd]()
    else:
        view.putln("Invalid command, runnning help")
        commands["help"]()

# ----------- Main game loop ----------- #

def start():
    global world, commands, scenes, current_scene

    world = World()
    commands = {
        "help": cmd_help, 
        "exit": cmd_exit, 
        "view": world.display_map, 
        "move south": partial(world.move_player, Direction.South), 
        "move east": partial(world.move_player, Direction.East), 
        "yell": cmd_yell }
    
    # These triplets are: (scene_loop, scene_enter, scene_exit)
    scenes = {
        "command_mode": (command_scene, None, None) }
    current_scene = "command_mode" # should start with "active_mode" or "menu"
    
    view.putcln("{bb}Welcome{} to {bk}moon-survival!{}")

def game_loop():
    scenes[current_scene][0]()

if __name__ == "__main__":
    start()
    while not should_exit:
        game_loop()