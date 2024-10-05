import pygame
import sys

class character:
  def __init__(self, level, speed, power, health, stamina):
    self.level = level
    self.speed = speed
    self.power = power
    self.health = health
    self.stamina = stamina

  def cook(self, stamina, health):
    if stamina > 0 and health > 0:
      print("DO YOU ACCEPT THE CHALLENGE?")
    return health, stamina

  
  def isAlive(self, health):
    if self.health >= 0:
      return health
    if self.health < 0:
      print("You have died :(")
      sys.exit()
      
  def levelUp(self, level, speed, stamina):
    if self.level == 1 and self.speed == 2 and self.stamina == 2:
      self.level += 1
    return level
  def speciality(self, power):
    if power == True:
      print("POWER CHARGED")
      return False

def choose_character(screen):
  global chara

  #render images
  blub = pygame.image.load("images/blue_char.png")
  purp = pygame.image.load("images/purp_char.png")
  one = pygame.image.load("images/one.png")
  two = pygame.image.load("images/two.png")
  blank_image = pygame.image.load("images/thunk.png")
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
    pygame.display.update()
    pygame.time.delay(2000)
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
  if chara == "blue":
    charac = character(1, 2, False, 10, 10)
    print("Level: " + str(charac.level) + " Speed: " + str(charac.speed) + 
    " Health: " + str(charac.health) + " Stamina: " + str(charac.stamina))
  if chara == "purp":
    charac = character(1,1,False, 20, 10)
    print("Level: " + str(charac.level) + " Speed: " + str(charac.speed) + 
      " Health: " + str(charac.health) + " Stamina: " + str(charac.stamina))
