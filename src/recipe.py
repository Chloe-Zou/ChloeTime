import time
import pygame, sys, random
from pygame.locals import K_r, KEYDOWN, K_SPACE, K_p
# from pygame.transform import scale
from timer2 import timey

onion_stew = pygame.image.load('images/Onion Stew.png')
ONION = pygame.image.load('images/hap.png')
potato = pygame.image.load('images/potato.png')
empty = pygame.image.load('images/empty.png')
soup = pygame.image.load('images/soup.png')
thunk = pygame.image.load("images/thunk.png")

def mean():
  words = ['you suck.', 'you are bad.', 'you are a loser.', 'you are a failure.',
           'you are so dumb', 'you are a disappointment', 'you are a disgrace',
           'you are a failure', 'why are you so disappointing?']
  x = random.randint(0, 8)
  print(words[x])
  time.sleep(2)
  print("...")

def scale_image(image, factor):
  return pygame.transform.scale(image, (image.get_width() * factor, image.get_height() * factor))

ONION = scale_image(ONION,1.5)
potato = scale_image(potato, 4)
thunk = scale_image(thunk, 20)
soup = scale_image(soup, 5)
empty = scale_image(empty, 5)

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
    print("EXAMPLE: if you want chop the onions, type 'onion'")
    ingSelect = "fishy"
    ingSelect = input("CHOOSE INGREDIENT: ")
    ingSelect = ingSelect.lower()
    time.sleep(.6)
    if ingSelect == "onion" or ingSelect == "onions":
      print(" ")
      print("CURRENTLY CHOPPING 'onion'")
      time.sleep(.5)
      screen.blit(thunk, (0,0))
      screen.blit(ONION, (50,0))
      pygame.display.update()
      print("Click on the onion and press space five times")
    else:
      time.sleep(1)
      mean()
      sys.exit()

    spacePressed = 0
    while True:
      for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_r:
          screen.blit(recimg, (130, 20))
          pygame.display.update()
        if event.type == KEYDOWN and event.key == K_SPACE:
          spacePressed +=1
          if spacePressed == 5 and ingSelect == "onion" or spacePressed == 5 and ingSelect == "onions":
            print("Onion: Good job chopping the onions!")
            time.sleep(.7)
            print("Onion: Now you cut the potatoes")
            ingSelect = input("CHOOSE INGREDIENT: ")
            ingSelect = ingSelect.lower()
            if ingSelect == "potato" or ingSelect == "potatoes":
              print(" ")
              print("CURRENTLY CHOPPING 'potato'")
              spacePressed = 0
              time.sleep(.5)
              screen.blit(thunk, (0,0))
              screen.blit(potato, (130, 20))
              pygame.display.update()
              print("Click on the potato and press space five times")
          if spacePressed == 5 and ingSelect == "potato" or spacePressed == 5 and ingSelect == "potatoes":
            print(" ")
            print("Onion: very nice :)")
            screen.blit(thunk, (0,0))
            pygame.display.update()
            
            time.sleep(.3)
            
            screen.blit(empty, (60, 0))
            pygame.display.update()
            
            print("Onion: To place the ingredients into the pot you click the pot and then press p")
        if event.type == KEYDOWN and event.key == K_p:
          print("Onion: Now you place the ingredients into the pot by typing the ingredient you want to add")
          print(" ")
          ing1 = input("CHOOSE INGREDIENT: ")
          ing1 = ing1.lower()
          time.sleep(.7)
          print("INGREDIENT ADDED: " + ing1)
          time.sleep(.7)
          more = input("Would you like to add another ingredient? (y/n)")
          if more == "y" or more == "yes":
            ing2 = input("CHOOSE INGREDIENT: ")
            ing2 = ing2.lower()
            time.sleep(.5)
            print("INGREDIENT ADDED: " + ing2)
            time.sleep(.6)
            print("Onion: Don't forget that we need chicken broth!!")
            more = input("Would you like to add another ingredient? (y/n)")
            if more == "y" or more == "yes":
              time.sleep(.2)
              ing3 = input("CHOOSE INGREDIENT: ")
              ing3 = ing3.lower()
              print("INGREDIENT ADDED: " + ing3)
              screen.blit(soup,(60,0))
              pygame.display.update()
              
              print("Onion: Now you will wait for it to be ready")
              time.sleep(.5)
              print("Onion: Wait for ten seconds before pressing 'l'")
              timey()
              print("work?")
          else:
            time.sleep(1)
            mean()
            sys.exit()
