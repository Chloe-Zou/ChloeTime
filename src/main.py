# Importing necessary libraries and setting up the initial environment
import pygame, sys
from pygame.locals import QUIT, KEYDOWN, K_1
from intro import importPhoto

global chara
global level
global speed
global power
global health
global stamina

#Set up pygame
pygame.init()
screen = pygame.display.set_mode((400, 300))
# pygame.display.set_caption('Welcome!')

# #load in images under a variable
start_image = pygame.image.load('images/start.png')


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

    screen.blit(current_image, (30, -90))
    pygame.display.update()

