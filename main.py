from terrain import Terrain

# ----------- Globals  ----------- #

terrain = Terrain()
should_exit = False

# ----------- Commands  ----------- #

def cmd_help():
    print("List of commands: ")
    print("\t", end="")
    for cmd_name in commands.keys():
        print(cmd_name, end=" ")
    print("\n", end="")

def cmd_exit():
    global should_exit
    should_exit = True
    print("Bye!")

def cmd_yell():
    print("Nobody hears you, as the moon has very little atmosphere.")

# ----------- Main game loop ----------- #

def start():
    print("Welcome to moon-survival!")

commands = {"help": cmd_help, "exit": cmd_exit, "view": terrain.display, "yell": cmd_yell}
def game_loop():
    print("> ", end="", flush=True)
    cmd = input()

    if cmd in commands:
        commands[cmd]()
    else:
        print("Invalid command, runnning help")
        commands["help"]()

if __name__ == "__main__":
    start()
    
    while not should_exit:
        game_loop()