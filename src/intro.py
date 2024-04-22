import pygame
import time

def importPhoto():
  pygame.init()
  screen = pygame.display.set_mode((400, 300))
  start_image = pygame.image.load('images/start.png')
  gramps = pygame.image.load('images/gramps.png')
  passed = pygame.image.load('images/gramps_dead.png')
  teacher = pygame.image.load('images/onion.png')
  bagu = pygame.image.load('images/BAGUETTE!!!.png')
  thunk = pygame.image.load('images/thunk.png')
  #Scale photos bigger
  scaling_factor = 2

  # Function to scale images
  def scale_image(image, factor):
      return pygame.transform.scale(image, (image.get_width() * factor, image.get_height() * factor))

  start_image = scale_image(start_image, scaling_factor)
  gramps = scale_image(gramps, scaling_factor)
  passed = scale_image(passed, scaling_factor)
  teacher = scale_image(teacher, scaling_factor)
  bagu = scale_image(bagu, scaling_factor)
  thunk = scale_image(thunk, scaling_factor)
 # Defining the start function which contains the start logic
  def start():
    global current_image
    global scaled_image
    name = input("ENTER YOUR NAME: ")
    current_image = gramps
    screen.blit(current_image, (15, -40))
    pygame.display.update()

    print(" ")
    print("ONE YEAR AGO")
    time.sleep(1)
    print("Gramps: Come here " + str(name))
    time.sleep(1.4)
    print("Gramps: When I was your age I always wanted to be a cook")
    time.sleep(1.7)
    print("Gramps: My goal was to become the best chef in the Catlands")
    time.sleep(1.8)
    print("Gramps: But now I am far too old for that :(")
    time.sleep(1.3)

    current_image = passed
    screen.blit(current_image, (15, -40))
    pygame.display.update()

    print(" ")
    print("Before Gramps died, he gave me his favorite spatula")
    time.sleep(1.2)
    print("So now I have decided to become a cook")
    time.sleep(.9)
    print("And achieve Gramps' dream")
    time.sleep(1.8)
    print("To do this I have found a teacher")

    current_image = teacher
    screen.blit(current_image, (15, -40))
    pygame.display.update()
    print(" ")
    time.sleep(1.5)
    print("This is Onion")
    time.sleep(.78)
    print("He specializes in French cuisine, and is highly regard in all the land")
    time.sleep(1.5)
    print("Onion: OUI, OUI, OUI, OUI, HON, HON, HON, HON, HON, HON, HON, HON ")
    time.sleep(2.3)
    print("I may not be able to understand his advanced vocabulary right now")
    time.sleep(1.5)
    print("But someday I will")
    time.sleep(1) 

    current_image = bagu
    screen.blit(current_image, (15, -40))
    pygame.display.update()

    print(" ")
    print("Onion: BAGUETTEEE!!!")
    time.sleep(1.5)
    print(" ")
    print("*thunk*")

    current_image = thunk
    screen.blit(current_image, (15, -40))
    pygame.display.update()

    time.sleep(.5)
    print(" ")
  start()
