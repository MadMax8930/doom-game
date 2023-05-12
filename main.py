import pygame as pg
import sys  #system module
from settings import *
from map import *

class Game:
   # in constructor we initialize the pygame modules
   def __init__(self):
      pg.init()
      self.screen = pg.display.set_mode(RES)  # creating screen for rendering the set resolution
      self.clock = pg.time.Clock()            # instance of the clock class for framer 8
      self.new_game()                         # call to the method from main app constructor
      
   def new_game(self):
      self.map = Map(self)                    # instance of the map class
   
   def update(self):
      pg.display.flip()                       # update the screen
      self.clock.tick(FPS)                    # display information about the current num of fps in the window caption
      pg.display.set_caption(f'{self.clock.get_fps() :.1f}')
      
   def draw(self):
      self.screen.fill('black')               # at each iteration we paint our screen in black
      self.map.draw()

   def check_events(self):
      for event in pg.event.get():            # check the events for closing the working window
         if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
            pg.quit()
            sys.exit()
      
   def run(self):
      while True:                             # main loop of the game
         self.check_events()              
         self.update()
         self.draw()
         
# instance of our game with run method call
if __name__ == '__main__':
   game = Game()
   game.run()