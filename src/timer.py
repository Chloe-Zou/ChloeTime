import pygame
import pygame.freetype
from pygame.locals import K_1, KEYDOWN, K_2


def result():
  pygame.init()
  screen = pygame.display.set_mode((400, 300))
  font = pygame.freetype.SysFont(None, 34)
  font.origin = True
  print(out)
  while font.origin:
    font.render_to(screen, (100, 100),  out, pygame.Color('dodgerblue'))
    pygame.display.flip()
    
def renderClock(screen):
  font.origin = True
  screen.fill(pygame.Color('grey12'))
  ticks = pygame.time.get_ticks()
  millis = ticks % 1000
  seconds = int(ticks / 1000 % 60)
  minutes = int(ticks / 60000 % 24)
  #formatting numbers
  out = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
  font.render_to(screen, (100,100), out, pygame.Color('dodgerblue'))
  pygame.display.flip()
  clock.tick(60)

def main():
  global out
  pygame.init()
  screen = pygame.display.set_mode((400, 300))
  clock = pygame.time.Clock()
  font = pygame.freetype.SysFont(None, 34)
  out = ''
  font.origin = True
  stopwatch_running = False
  while True:
    for e in pygame.event.get():
      if e.type == KEYDOWN and e.key == K_1:
        font.origin = False
        return font.origin
      if e.type == KEYDOWN and e.key == K_2:
        renderClock(screen)

main()
result()
