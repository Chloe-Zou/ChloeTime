import time
import pygame
from pygame.locals import K_r, KEYDOWN, K_SPACE

onion_stew = pygame.image.load('images/Onion Stew.png')
recimg = onion_stew

def recipe(num):
  global recipe
  if num == 0:
    print("Onion: You have to cook an onion stew.")
    time.sleep(.7)
    print("Onion: Here is your recipe")
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    screen.blit(recimg, (130, 20))
    pygame.display.update()
    time.sleep(5)
    print("Onion: If you ever need to see the recipe again, just press 'r'")
    time.sleep(2)
    print("Onion: To chop the ingredients press space 5 times")
    time.sleep(1)
    print("Onion: To select the ingredient to chop just type the name")
    time.sleep(1)
    ingSelect = "fishy"
    ingSelect = input("CHOOSE INGREDIENT: ")
    ingSelect = ingSelect.lower()
    time.sleep(.6)
    if ingSelect == "onion":
      print("CURRENTLY CHOPPING 'onion'")
      time.sleep(.5)
      print("Click on the onion and press space five times")
    if ingSelect == "potato" or ingSelect == "potatoes":
      print("CURRENTLY CHOPPING 'potato'")
      print("Click on the potato and press space five times")

    spacePressed = 0
    while True:
      for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_r:
          screen = pygame.display.set_mode((400, 300))
          screen.blit(recimg, (130, 20))
          pygame.display.update()
        if event.type == KEYDOWN and event.key == K_SPACE:
          spacePressed +=1
          if spacePressed == 5 and ingSelect == "onion":
            print("Onion: Good job chopping the onions!")
            time.sleep(.7)
            print("Onion: Now you cut the potatoes")
            ingSelect = input("CHOOSE INGREDIENT: ")
            ingSelect = ingSelect.lower()
          if spacePressed == 5 and ingSelect == "potato":
            print("Onion: very nice :)")
            time.sleep(.3)
            print("Onion: To place the ingredients into the pot")
            
  
