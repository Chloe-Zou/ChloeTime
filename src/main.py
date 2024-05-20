# Importing necessary libraries and setting up the initial environment
import pygame, sys
import time
from pygame.locals import QUIT, KEYDOWN, K_1, K_2
from intro import importPhoto
from character import choose_character, chara_stats
from recipe import recipe

#Set up pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Welcome!')

# #load in images under a variable
start_image = pygame.image.load('images/start.png')
thunk = pygame.image.load('images/thunk.png')  
x = 0

print("PRESS 1 TO BEGIN")
print("PRESS 2 TO SKIP THE INTRO")

# def win():
#     if charac.health > 0:
#         print("YOU WIN!")
# def loss():
def cookOff():
    recipe(x)

# Setting the initial image to start_image
current_image = start_image

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_1:
                importPhoto()
                choose_character(screen)
                chara_stats()
                time.sleep(2)
                print(" ")
                cookOff()
                time.sleep(9)
                current_image = thunk
                sys.exit()
            if event.key == K_2:
                screen.blit(thunk, (100,0))
                choose_character(screen)
                chara_stats()
                time.sleep(2)
                print(" ")
                cookOff()
                sys.exit()


    screen.blit(current_image, (100, 0))
    pygame.display.update()

