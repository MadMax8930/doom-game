## Doom Game in Python
Based on the ray-casting algorithm

### Development plan

- Implement a two-dimensional plan with three-dimensional illusion of space (pseudo 3D)
- Create an efficient and fast 2D ray-caster, where we cast a number of rays in a certain FOV of the player
   - For each ray, an intersection point with the wall needs to be found
   - Implement the 3D projection of the game level
   - Apply various textures and embed sprites
   - Build smart and full-fledged enemies (Pathfinding algorithm)
   - Add sounds for specific game events

### Dependency

```bash
pip install pygame
```

### File Structure

- main.py: Main application template
- map_game.py: Game world
- npc.py: Enemy logic
- object_handler.py : Add sprites
- object_renderer.py : Access textures
- raycasting.py : Engine of the game
- settings.py : Screen resolution, Frame rate & different variables
- sound.py : specific game event sounds
