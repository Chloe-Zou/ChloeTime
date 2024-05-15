import pygame
import pygame.freetype
from pygame.locals import K_1, KEYDOWN, K_2

global out

def start():
  global out
  start_time = 0
  ticks = pygame.time.get_ticks() - start_time
  millis = ticks % 1000
  seconds = int(ticks / 1000 % 60)
  minutes = int(ticks / 60000 % 24)
  out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)

def result():
  pygame.init()
  screen = pygame.display.set_mode((400, 300))
  font = pygame.freetype.SysFont(None, 34)
  font.origin = True
  print(out)
  while font.origin:
    font.render_to(screen, (100, 100),  out, pygame.Color('dodgerblue'))
    pygame.display.flip()

def main():
  pygame.init()
  screen = pygame.display.set_mode((400, 300))
  clock = pygame.time.Clock()
  font = pygame.freetype.SysFont(None, 34)
  font.origin = True
  stopwatch_running = False
  while True:
    for e in pygame.event.get():
      if e.type == KEYDOWN and e.key == K_1:
        font.origin = False
        return font.origin
      if e.type == KEYDOWN and e.key == K_2:
        stopwatch_running = True
        start()

      # Inside the main game loop
      if stopwatch_running:
        font.render_to(screen, (100, 100), out, pygame.Color('dodgerblue'))
        pygame.display.flip()
        clock.tick(60)

main()
result()
