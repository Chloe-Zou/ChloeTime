import pygame

class character:
  def __init__(self, level, speed, power, health, stamina):
    self.level = level
    self.speed = speed
    self.power = power
    self.health = health
    self.stamina = stamina

def choose_character(screen):
  global chara

  #render images
  blub = pygame.image.load("blue_char.png")
  purp = pygame.image.load("purp_char.png")
  one = pygame.image.load("one.png")
  two = pygame.image.load("two.png")
  blank_image = pygame.image.load("thunk.png")
  screen.blit(blub, (-30, 0))
  screen.blit(purp, (90, 0))
  screen.blit(one, (50, 140))
  screen.blit(two, (170, 140))
  pygame.display.update()

  chose = input("CHOOSE YOUR CHARACTER: ")
  if chose == "1":
    screen.blit(blank_image, (-30, 0))
    screen.blit(blank_image, (90, 0))
    screen.blit(blank_image, (50, 140))
    screen.blit(blank_image, (170, 140))
    pygame.display.update()
    print("CHARACTER CHOSEN: BLUB")
    screen.blit(blub, (60,0))
    pygame.time.delay(500000)
    pygame.display.update()
    chara = "blue"

  if chose == "2":
    screen.blit(blank_image, (-30, 0))
    screen.blit(blank_image, (90, 0))
    screen.blit(blank_image, (50, 140))
    screen.blit(blank_image, (170, 140))
    pygame.display.update()
    print("CHARACTER CHOSEN: PURP")
    screen.blit(purp, (60, 0))
    pygame.display.update()
    chara = "purp"

def chara_stats():
  global chara
  global level
  global speed
  global power
  global health
  global stamina

  level = 0
  speed = 0
  power = False
  health = 0
  stamina = 0

  if chara == "blue":
    level = 1
    speed = 2
    power = False
    health = 10
    stamina = 10
  if chara == "purp":
    level = 1
    speed = 1
    power = False
    health = 20
    stamina = 10
