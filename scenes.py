import curses
import view

current_scene = None # is the actual object
scenes = {}

def init_scenes(init_scene, window, world):
    global current_scene
    scenes["terminal_mode"] = Terminal(window, world)
    scenes["control_mode"] = Control(window, world)
    change_scene_to(init_scene)

def loop_current_scene():
    current_scene.loop()

def exit_scenes():
    current_scene.exit()

def change_scene_to(scene_name):
    global current_scene
    current_scene = scenes[scene_name]
    current_scene.enter()

class Scene:
    def enter(self):
        pass

    def loop(self):
        pass

    def exit(self):
        pass

# ----------- Scenes ----------- #

class Terminal(Scene):
    def __init__(self, window, world):
        self.window = window
        self.world = world

    def enter(self):
        curses.curs_set(1)
        curses.echo()
        curses.nocbreak()
        self.window.keypad(True)

        self.window.move(0, 0)
        view.putcolor(self.window, "{bb}Welcome{} to {bk}moon-survival!{}")

        self.window.move(1, 0)
        self.window.refresh()

    def loop(self):
        y, x = self.window.getyx()
        self.window.addstr(y, 0, "> ")
        self.window.refresh()

        #view.put("> ", flush=True)
        # TODO: figure out how to get input using curses.
        cmd = input()
        self.window.move(y+1, 0)

        if cmd in commands:
            commands[cmd]()
        else:
            view.putln("Invalid command, runnning help")
            commands["help"]()
        
        self.window.refresh()

class Control(Scene):
    def __init__(self, window, world):
        self.window = window
        self.world = world

    def enter(self):
        curses.curs_set(0)
        curses.noecho()
        curses.cbreak()
        self.window.keypad(True)

    def loop(self):
        view.put("> ", flush=True)
        cmd = input()

        if cmd in commands:
            commands[cmd]()
        else:
            view.putln("Invalid command, runnning help")
            commands["help"]()
        
        self.window.refresh()