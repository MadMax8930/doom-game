import pygame as pg

# Two dimensional array (1: wall , False: space)
_ = False
mini_map = [
   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
   [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
   [1, _, _, 1, 1, 1, 1, _, _, _, 1, 1, 1, _, _, 1],
   [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
   [1, _, _, _, _, _, 1, _, _, _, _, _, 1, _, _, 1],
   [1, _, _, 1, 1, 1, 1, _, _, _, _, _, _, _, _, 1],
   [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
   [1, _, _, 1, _, _, _, 1, _, _, _, _, _, _, _, 1],
   [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Instance of the game class as input to the constructor
class Map:
   def __init__(self, game):
      self.game = game
      self.mini_map = mini_map
      self.world_map = {}
      self.get_map()
      
   # World map obtained through a separate method which we iterate over our array
   # and write coordinated of elements with only numeric values to the dictionary  
   def get_map(self):
      for j, row in enumerate(self.mini_map):
         for i, value in enumerate(row):
            if value:
               self.world_map[(i, j)] = value
               
   # Iterating over the world map we will draw each element of the map as an unfilled square
   def draw(self):
      [pg.draw.rect(self.game.screen, 'darkgray', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
      for pos in self.world_map]