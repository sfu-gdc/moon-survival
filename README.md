# moon-survival
a text-based game about surviving on the moon

### info:
- version: python 3.7 or greater
- structure: the codebase is structured as MVC (model-view-controller). The partitions are: World (model), view, and main (controller). If any information is needed or actions need to be taken, it is best to talk to the world, rather than store object handles everywhere.
-

### instructions:
- in order to input a command, press \[e\] to go to your inventory.

### tasks:
- add a menu
- implement semi-realtime command interface
  - improve key input w/ up-arrow last-thing & copy paste.
- better terrain generation:
  - more quadrants
  - generate resources at world start
  - switch to a procedurally generated & chunk based terrain system
- implement an inventory
- create & design enemies
  - multi-tile enemies 
- implement electricity as a resource
- creation of buildings
  - management of air & other gasses
  - farming
  - rooms that have different purposes
  - incentive towards placing rooms in specific orientations -> "ethereum field"
- atmospheric change & effects
- production & processing of resources, kinda like factorio
- commands should be unlocked over time
- ...

### completed tasks:
- .

### installation:
- run `pip3 install -r requirements.txt` or alternately `pip install -r requirements.txt` to install dependencies.
- for people running on linux, you may need to do `sudo apt-get install -y python3-dev libasound2-dev`
- Note: wsl doesn't natively support audio
- 