# moon-survival
a text-based game about surviving on the moon

### info:
- version: python3.7 -> aim is to make it relatively python3-agnostic.
- 

### structure:

The codebase is structured as a modified MVC (model-view-controller). The main 3 partitions are: World, view, and controller, however world and controller are more connected than not. If any information is needed or actions need to be taken, it is best to query & talk to the world, rather than hold various object handles all over the place.

### tasks:
- implement semi-realtime command interface
- better terrain generation:
- - more quadrants
- - generate resources at world start
- implement an inventory
- create & design enemies 
- ...


### completed tasks:
- 