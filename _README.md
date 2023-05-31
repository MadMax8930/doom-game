## Doom Game base on the ray-casting algorithm

- Two-dimensional plan with three-dimensional illusion of space (pseudo 3d)
- Efficient and fast 2d ray-caster
   - 3d projection of the game level
   - Apply various textures and embed sprites
   - Make smart and full-fledged enemies (Pathfinding algorithm)

### Dependencies

- pip install pygame

### Ray Casting

Cast a given number of rays in a certain fow of the player and for each ray, we need to determine the intersection point with the wall

### File Structure

- main.py: Main application template
- map_game.py: Game world
- npc.py: Enemy logic
- settings.py : Screen resolution & Frame rate
- raycasting.py : Engine of the game
- object_renderer.py : Access textures
