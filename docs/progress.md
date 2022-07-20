# Dinosaur game AI journal

## Tuesday 19th (20220719)

 - Set up a development environment for python arcade [URL]
 - Starting with the game example from RealPython [URL] extended the `arcade.Window class` (GameScreen) to draw players, enemies and backgrounds using the list-draw system from arcade.
 - Created a `Player` class off of the `arcade.Sprite` class
 - Implemented rudimentary physics by hand (TODO: Use arcade physics)
 - Implemented a jump system for the dinosaur
 - Updated the graphics with an image and a hardcoded border
 
## Wednesday 20th (20220720)

 - Refactored the single file into a package containing a `gamescreen` and player `module`; constants are loaded from the `__init__` (TODO: Offoad the constants to a constants module)
 - Created an enemy module based on the `player` module
 - Updated the relevant graphics (similar to the `Player` graphics) [SCREENSHOT]
 - Started progress documentation
