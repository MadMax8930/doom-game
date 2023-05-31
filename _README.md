## Doom Game base on the ray-casting algorithm

- Two-dimensional plan with three-dimensional illusion of space (pseudo 3d)
- Efficient and fast 2d ray-caster
   - 3d projection of the game level
   - Apply various textures and embed sprites
   - Make smart and full-fledged enemies (can't hide -> Path-finding algorithm)

### Dependencies

- pip install pygame

### Ray Casting

Cast a given number of rays in a certain fow of the player and for each ray, we need to determine the intersection point with the wall

### File Structure

- main.py: Main application template
- map_game.py: Game world
- settings.py : Screen resolution & Frame rate
- raycasting.py : Engine of the game
- object_renderer.py : Access textures


pg.display.flip()                                # update the screen

game def __init__                       # in constructor we initialize the pygame modules
self.screen = pg.display.set_mode(RES)  # creating screen for rendering the set resolution
self.clock = pg.time.Clock()            # instance of the clock class for frame rate
self.delta_time = 1                     # Delta time: is the amount of time that has passed since the last frame
->  # If we want the player's movement speed to be independent of the frame rate, we need to get the Delta time value for each frame
