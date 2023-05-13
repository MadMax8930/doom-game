import pygame as pg
from settings import *

class ObjectRenderer:
   def __init__(self, game):
      self.game = game
      self.screen = game.screen
      self.wall_textures = self.load_wall_textures() # access textures through this attribute
      
   @staticmethod
   def get_textures(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
      texture = pg.image.load(path).convert_alpha()
      return pg.transform.scale(texture, res)
   
   def load_wall_textures(self):
      return {
         1: self.get_textures('resources/textures/wall_1.png'),
         2: self.get_textures('resources/textures/wall_2.png'),
         3: self.get_textures('resources/textures/wall_3.png'),
         4: self.get_textures('resources/textures/wall_4.png'),
         5: self.get_textures('resources/textures/wall_5.png'),
      }