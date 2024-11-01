# How to play the game
After implementing `nearest_bee`, a `ThrowerAnt` should be able to `throw_at` a `Bee` in front of it that is not still in the `Hive`.

Now you're ready to try what you've built. To start a graphical game, run:

`python3 gui.py`
After you start the graphical version, the game is (usually) available at http://127.0.0.1:31415/.

The game has several options that you will use throughout the project, which you can view with `python3 gui.py --help`.

``` bash
usage: gui.py [-h] [-d DIFFICULTY] [-w] [--food FOOD]

Play Ants vs. SomeBees

optional arguments:
  -h, --help     show this help message and exit
  -d DIFFICULTY  sets difficulty of game (test/easy/normal/hard/extra-hard)
  -w, --water    loads a full layout with water
  --food FOOD    number of food to start with when testing
```
You can refresh the webpage to restart the game, but if you changed your code, you need to terminate `gui.py`and run it again. To terminate `gui.py`, you can hit `Ctrl + C` on the terminal.

You cannot have multiple tabs of this same Ants GUI open simultaneously or they will all error.