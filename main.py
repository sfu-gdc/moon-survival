from world import World
import view

# ----------- Globals  ----------- #

world = None
should_exit = False
commands = None

# ----------- Commands  ----------- #

def cmd_help():
    view.putcln("{bm}List of commands: {}")
    view.put("\t")
    view.putlist(commands.keys(), delim=" ", newline=True)

def cmd_exit():
    global should_exit
    should_exit = True
    view.putln("Bye!")

def cmd_yell():
    view.putcln("{y}Nobody hears you, as the moon has very little atmosphere.{}")

# ----------- Main game loop ----------- #

def start():
    global world, commands
    world = World()
    commands = {
        "help": cmd_help, 
        "exit": cmd_exit, 
        "view": world.display_terrain, 
        "yell": cmd_yell }
    
    view.putcln("{bb}Welcome{} to {bk}moon-survival!{}")

def game_loop():
    view.put("> ", flush=True)
    cmd = input()

    if cmd in commands:
        commands[cmd]()
    else:
        view.putln("Invalid command, runnning help")
        commands["help"]()

if __name__ == "__main__":
    start()
    while not should_exit:
        game_loop()